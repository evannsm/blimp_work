import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Quaternion, Vector3, Point
from mocap_msgs.msg import RigidBodies
from std_msgs.msg import Float32MultiArray
from nav_msgs.msg import Odometry
import numpy as np

from . utilities import *

from . BlimpSim import BlimpSim
from . BlimpLogger import BlimpLogger

import sys

import time
import csv

class BlimpMPCNode(Node):
    def __init__(self, controller, logfile, blimp_id=0):
        super().__init__(f'blimp_mpc_{blimp_id}')
        
        # time.sleep(7.5)

        self.logfile = logfile

        # Create periodic controller "interrupt"
        self.dT = controller.dT
        self.timer = self.create_timer(self.dT, self.compute_control)

        # Create publisher for sending commands to blimp    
        self.publisher_ = self.create_publisher(
            Quaternion,
            f"/agents/blimp{blimp_id}/motion_command",
            10
        )

        # Create publisher to sending state data to rta
        self.state_publisher = self.create_publisher(
            Odometry,
            f"/agents/blimp{blimp_id}/state",
            1
        )

        # Create subscribers for reading state data
        
        self.update_mocap_subscription = self.create_subscription(
            RigidBodies,
            f"/rigid_bodies",
            self.read_mocap,
            1
        )

        # Create subscriber for updating the trajectory from an RTA node.
        self.trajectory_subscription = self.create_subscription(
            Float32MultiArray,
            f'/agents/blimp{blimp_id}/trajectory', #reference_trajectory'
            self.read_trajectory,
            1
        )

        try:
            self.rta_dT = controller.rta_dT # May or may not exist.
            self.timer_ = self.create_timer(self.rta_dT, self.publish_state)
        except AttributeError:
            self.get_logger().warn(f'no RTA dT set for this controller.')
        
        # Create controller and "simulator" variables
        
        self.mocap_read_times = []

        self.controller = controller

        # The "simulator" is just a dummy object that passes along data from
        # the actual blimp. The blimp controller classes require a "simulator"
        # to exist, from which they read the state data.
        self.sim = BlimpSim(self.dT)

        # Used for computing derivatives
        self.pos_history = None    # [x, y, z]
        self.vel_history = None    # [vx, vy, vz]
        self.ang_history = None       # [phi, theta, psi]
        self.d_ang_history = None     # [wx, wy, wz]

        self.d_pos_history = None
        self.d_vel_history = None
        self.d_ang_history = None
        self.d_avl_history = None

        self.full_rotations = 0
        self.prev_mocap_psi = None

        self.last_mocap_timestamp = None
        self.last_gyro_timestamp = None
        self.mocap_k = -1   # index of most recent mocap msg in state history arrays
        self.gyro_k = -1    # index of most recent gyro msg in angle history array

        self.state_variables_valid = False
        
        self.data_block_length = 5

        self.theta_0 = 0
        self.phi_0 = 0

    def read_velocities(self, msg):
        self.vel_last_message = msg

    def read_angles(self, msg):
        self.angles_last_message = msg

    def read_mocap(self, msg):
        blimp = msg.rigidbodies[0]

        self.mocap_read_times.append(msg.header.stamp.sec + msg.header.stamp.nanosec*1e-9)

        self.mocap_k += 1

        # Mocap gives you x, y, z, phi, theta, psi
        # Can compute vx, vy, vz

        x = blimp.pose.position.x
        y = blimp.pose.position.y
        z = blimp.pose.position.z

        angles = quat2euler(np.array([blimp.pose.orientation.x,
                                      blimp.pose.orientation.y,
                                      blimp.pose.orientation.z,
                                      blimp.pose.orientation.w]))
        
        phi = angles[0] - self.phi_0
        theta = angles[1] - self.theta_0
        mocap_psi = angles[2]

        if self.mocap_k == 0:
            # Initialize the roll and pitch angles to be zero.
            self.phi_0 = phi
            self.theta_0 = theta

        psi = None
        
        if self.mocap_k == 0:
            self.prev_mocap_psi = mocap_psi
            psi = mocap_psi

        elif self.mocap_k > 0:
            # mocap angles are from -pi to pi, whereas the angle state variable
            # in the MPC is an absolute angle (i.e. no modulus)
            
            # I correct for this discrepancy here

            if self.prev_mocap_psi > np.pi*0.9 and mocap_psi < -np.pi*0.9:
                # Crossed 180 deg, CCW
                self.full_rotations += 1

            elif self.prev_mocap_psi < -np.pi*0.9 and mocap_psi > np.pi*0.9:
                # Crossed 180 deg, CW
                self.full_rotations -= 1

            psi = mocap_psi + 2*np.pi * self.full_rotations

            self.prev_mocap_psi = mocap_psi

        current_pos_vector = np.array([x, y, z]).reshape((3,1))
        current_ang_vector = np.array([phi, theta, psi]).reshape((3,1))

        if self.pos_history is None:
            self.pos_history = np.array(current_pos_vector).reshape((3, 1))
        else:
            x_avg = 0.3*self.pos_history[0, -1] + 0.7*x
            y_avg = 0.3*self.pos_history[1, -1] + 0.7*y
            z_avg = 0.3*self.pos_history[2, -1] + 0.7*z
            current_pos_vector = np.array([x_avg, y_avg, z_avg]).reshape((3,1))
            self.pos_history = np.hstack((self.pos_history, current_pos_vector))
         
        if self.ang_history is None:
            self.ang_history = np.array(current_ang_vector).reshape((3, 1))
        else:      
            phi_avg = 0.3*self.ang_history[0, -1] + 0.7*phi
            theta_avg = 0.3*self.ang_history[1, -1] + 0.7*theta
            psi_avg = 0.3*self.ang_history[2, -1] + 0.7*psi
            current_ang_vector = np.array([phi_avg, theta_avg, psi_avg]).reshape((3,1))
            self.ang_history = np.hstack((self.ang_history, current_ang_vector))

        if self.mocap_k == 0:
            self.vel_history = np.array([0, 0, 0], dtype=np.float64).reshape((3,1))
            self.avl_history = np.array([0, 0, 0], dtype=np.float64).reshape((3,1))

            self.d_pos_history = np.array([0, 0, 0], dtype=np.float64).reshape((3,1))
            self.d_vel_history = np.array([0, 0, 0], dtype=np.float64).reshape((3,1))
            self.d_ang_history = np.array([0, 0, 0], dtype=np.float64).reshape((3,1))
            self.d_avl_history = np.array([0, 0, 0], dtype=np.float64).reshape((3,1))
        elif self.mocap_k < self.data_block_length:
            self.vel_history = np.hstack((self.vel_history,
                                          np.array([0, 0, 0]).reshape((3,1))))
            self.avl_history = np.hstack((self.avl_history,
                                          np.array([0, 0, 0]).reshape((3,1))))
            self.d_pos_history = np.hstack((self.d_pos_history,
                                          np.array([0, 0, 0]).reshape((3,1))))
            self.d_vel_history = np.hstack((self.d_vel_history,
                                          np.array([0, 0, 0]).reshape((3,1))))
            self.d_ang_history = np.hstack((self.d_ang_history,
                                          np.array([0, 0, 0]).reshape((3,1))))
            self.d_avl_history = np.hstack((self.d_avl_history,
                                          np.array([0, 0, 0]).reshape((3,1))))
        else:
            deltaT = self.mocap_read_times[-1] - self.mocap_read_times[-1-self.data_block_length]
            
            x_dot_raw = (self.pos_history[0][self.mocap_k]
                    - self.pos_history[0][self.mocap_k-self.data_block_length]) / deltaT
            y_dot_raw = (self.pos_history[1][self.mocap_k]
                    - self.pos_history[1][self.mocap_k-self.data_block_length]) / deltaT
            z_dot_raw = (self.pos_history[2][self.mocap_k]
                    - self.pos_history[2][self.mocap_k-self.data_block_length]) / deltaT
            
            filter_coeffs = np.array([0.1, 0.15, 0.15, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05], dtype=np.float64)
            if deltaT > 0.1:
                x_dot = filter_coeffs[0] * x_dot_raw
                y_dot = filter_coeffs[0] * y_dot_raw
                z_dot = filter_coeffs[0] * z_dot_raw
                
                for i in range(1, len(filter_coeffs)):
                    if i > self.d_pos_history.shape[1]:
                        break
                
                    x_dot += filter_coeffs[i] * self.d_pos_history[0, -i]
                    y_dot += filter_coeffs[i] * self.d_pos_history[1, -i]
                    z_dot += filter_coeffs[i] * self.d_pos_history[2, -i]
            else:
                x_dot = x_dot_raw
                y_dot = y_dot_raw
                z_dot = z_dot_raw

            pos_dot = np.array([x_dot, y_dot, z_dot]).T
            
            self.d_pos_history = np.hstack((self.d_pos_history,
                                              pos_dot.reshape((3,1))))
            
            vel_vect_b = R_b__n_inv(phi_avg, theta_avg, psi_avg) @ pos_dot
            self.vel_history = np.hstack((self.vel_history, vel_vect_b.reshape((3,1))))
            
            d_vel = (self.vel_history[:, self.mocap_k] - self.vel_history[:, self.mocap_k-1]) / deltaT
            self.d_vel_history = np.hstack((self.d_vel_history, d_vel.reshape((3,1))))
           

            phi_dot_raw = (self.ang_history[0][self.mocap_k]
                       - self.ang_history[0][self.mocap_k-self.data_block_length]) / deltaT
            theta_dot_raw = (self.ang_history[1][self.mocap_k]
                       - self.ang_history[1][self.mocap_k-self.data_block_length]) / deltaT
            psi_dot_raw = (self.ang_history[2][self.mocap_k]
                       - self.ang_history[2][self.mocap_k-self.data_block_length]) / deltaT
            
            if deltaT > 0.1:
                phi_dot = filter_coeffs[0] * phi_dot_raw
                theta_dot = filter_coeffs[0] * theta_dot_raw
                psi_dot = filter_coeffs[0] * psi_dot_raw

                for i in range(1, len(filter_coeffs)):
                    if i > self.d_ang_history.shape[1]:
                        break
                
                    phi_dot += filter_coeffs[i] * self.d_ang_history[0, -i]
                    theta_dot += filter_coeffs[i] * self.d_ang_history[1, -i]
                    psi_dot += filter_coeffs[i] * self.d_ang_history[2, -i]

            else:                
                phi_dot = phi_dot_raw
                theta_dot = theta_dot_raw
                psi_dot = psi_dot_raw
                    
            ang_dot = np.array([phi_dot, theta_dot, psi_dot]).T
            
            self.d_ang_history = np.hstack((self.d_ang_history,
                                              ang_dot.reshape((3,1))))
                
            ang_vel_b = np.linalg.inv(T(phi_avg, theta_avg)) @ ang_dot
            self.avl_history = np.hstack((self.avl_history, ang_vel_b.reshape((3,1))))
            
            d_ang_vel = (self.d_ang_history[:, self.mocap_k] - self.d_ang_history[:, self.mocap_k-1]) / deltaT
            self.d_avl_history = np.hstack((self.d_avl_history, d_ang_vel.reshape((3,1))))

    def publish_state(self):
        if self.pos_history is None \
            or self.vel_history is None \
            or self.ang_history is None \
            or self.d_ang_history is None \
            or self.d_pos_history is None \
            or self.d_vel_history is None \
            or self.d_ang_history is None \
            or self.d_avl_history is None:
            return # No valid state to publish.

        x = self.pos_history[0][self.mocap_k]
        y = self.pos_history[1][self.mocap_k]
        z = self.pos_history[2][self.mocap_k]

        v_x = self.vel_history[0][self.mocap_k]
        v_y = self.vel_history[1][self.mocap_k]
        v_z = self.vel_history[2][self.mocap_k]

        phi = self.ang_history[0][self.mocap_k]
        theta = self.ang_history[1][self.mocap_k]
        psi = self.ang_history[2][self.mocap_k]

        w_x = self.avl_history[0][self.gyro_k]
        w_y = self.avl_history[1][self.gyro_k]
        w_z = self.avl_history[2][self.gyro_k]

        # Organize the above into an odometry message.
        msg = Odometry()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'world'
        msg.child_frame_id = 'blimp'
        
        msg.pose.pose.position.x = x
        msg.pose.pose.position.y = y
        msg.pose.pose.position.z = z # = Point(x, y, z)
        
        # print(type(v_x)) # TODO: delete

        msg.twist.twist.linear.x = v_x
        msg.twist.twist.linear.x = v_y
        msg.twist.twist.linear.z = v_z
        
        msg.pose.pose.orientation.x = phi # we are not using Quaternions.
        msg.pose.pose.orientation.y = theta
        msg.pose.pose.orientation.z = psi

        msg.twist.twist.angular.x = w_x
        msg.twist.twist.angular.y = w_y
        msg.twist.twist.angular.z = w_z

        self.state_publisher.publish(msg)


    def read_trajectory(self, msg):
        self.get_logger().error('reading the trajectory')
        # Get the trajectory from the RTA node, and pass it to the controller object.
        trajectory_raw = msg.data
        trajectory_dim0 = msg.layout.dim[0].size
        trajectory_dim1 = msg.layout.dim[1].size
        trajectory = np.empty((trajectory_dim0, trajectory_dim1))

        # trajectory_raw is a list. Convert it to a numpy array of the appropriate dimensions
        for i in range(trajectory_dim0):
            for j in range(trajectory_dim1):
                trajectory[i, j] = trajectory_raw[i*trajectory_dim1 + j]

        # get (x,y,z,psi,v_x,v_y,v_z,psi_dot)
        if trajectory.shape[0] > 12:
            trajectory = trajectory[[6,7,8,11,0,1,2,5,12,13,14,15],:]
        else:
            trajectory = trajectory[[4,5,6,7,0,1,2,3],:]
            # trajectory = trajectory[[6,7,8,11,0,1,2,5],:] # If GurobiTryAgainLol

        self.controller.update_rta_trajectory(trajectory)

    def compute_control(self):
        
        if self.pos_history is None \
            or self.vel_history is None \
            or self.ang_history is None \
            or self.d_ang_history is None \
            or self.d_pos_history is None \
            or self.d_vel_history is None \
            or self.d_ang_history is None \
            or self.d_avl_history is None:
            return

        x = self.pos_history[0][self.mocap_k]
        y = self.pos_history[1][self.mocap_k]
        z = self.pos_history[2][self.mocap_k]

        v_x = self.vel_history[0][self.mocap_k]
        v_y = self.vel_history[1][self.mocap_k]
        v_z = self.vel_history[2][self.mocap_k]

        phi = self.ang_history[0][self.mocap_k]
        theta = self.ang_history[1][self.mocap_k]
        psi = self.ang_history[2][self.mocap_k]

        w_x = self.avl_history[0][self.gyro_k]
        w_y = self.avl_history[1][self.gyro_k]
        w_z = self.avl_history[2][self.gyro_k]

        self.sim.set_var('x', x)
        self.sim.set_var('y', y)
        self.sim.set_var('z', z)
        self.sim.set_var('vx', v_x)
        self.sim.set_var('vy', v_y)
        self.sim.set_var('vz', v_z)
        self.sim.set_var('phi', phi)
        self.sim.set_var('theta', theta)
        self.sim.set_var('psi', psi)
        self.sim.set_var('wx', w_x)
        self.sim.set_var('wy', w_y)
        self.sim.set_var('wz', w_z)
        
        self.sim.set_var_dot('x', self.d_pos_history[0][self.mocap_k])
        self.sim.set_var_dot('y', self.d_pos_history[1][self.mocap_k])
        self.sim.set_var_dot('z', self.d_pos_history[2][self.mocap_k])
        self.sim.set_var_dot('phi', self.d_ang_history[0][self.mocap_k])
        self.sim.set_var_dot('theta', self.d_ang_history[1][self.mocap_k])
        self.sim.set_var_dot('psi', self.d_ang_history[2][self.mocap_k])
        self.sim.set_var_dot('vx', self.d_vel_history[0][self.mocap_k])
        self.sim.set_var_dot('vy', self.d_vel_history[1][self.mocap_k])
        self.sim.set_var_dot('vz', self.d_vel_history[2][self.mocap_k])
        self.sim.set_var_dot('wx', self.d_avl_history[0][self.gyro_k])
        self.sim.set_var_dot('wy', self.d_avl_history[1][self.gyro_k])
        self.sim.set_var_dot('wz', self.d_avl_history[2][self.gyro_k])
        
        if not self.controller.is_initialized:
            self.controller.init_sim(self.sim)
        
        t0 = time.time()
        ctrl = self.controller.get_ctrl_action(self.sim)
        print(f"Control Time: {time.time()-t0}")
        if ctrl is None:
            self.write_command(0.0, 0.0, 0.0, 0.0)
            print(f'[ERROR] ctrl is {ctrl}.')
            sys.exit(0)
            
        fx = ctrl[0].item()
        fy = ctrl[1].item()
        fz = ctrl[2].item()
        tau_z = ctrl[3].item()
        
        self.sim.u = ctrl
        self.sim.update_history()

        print()
        print(f"State: {round(x, 6)}, {round(y, 6)}, {round(z, 6)}, {round(psi, 6)}\nControl: {round(fx, 6)}, {round(fy, 6)}, {round(fz, 6)}, {round(tau_z, 6)}")

        self.write_command(fx, fy, fz, tau_z)

    def write_command(self, fx, fy, fz, tau_z):

        msg = Quaternion()

        msg.x = fx
        msg.y = fy
        msg.z = fz
        msg.w = tau_z
        
        self.publisher_.publish(msg)

    def destroy_node(self):
        print("Logging data...")
        logger = BlimpLogger(self.logfile)
        logger.log(self.sim, self.controller)
        print("Logging done!")
