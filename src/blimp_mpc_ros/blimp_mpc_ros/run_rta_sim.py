# from . BlimpSim import BlimpSim
from gtmab_model.BlimpSim import BlimpSim
from . BlimpLogger import BlimpLogger

import numpy as np
import sys
import time

from geometry_msgs.msg import Quaternion, Pose, Point
from mocap_msgs.msg import RigidBodies, RigidBody

from . utilities import *

import rclpy
from rclpy.node import Node

# New idea: write this as a pub/sub node that
# synthesizes mocap data by simulating blimp dynamics, and
# receives motion_command as inputs to the blimp.

class RunRtaSimNode(Node):
    def __init__(self, logfile, dT=0.01, blimp_id=0):
        super().__init__(f'run_rta_sim_node')
        self.logfile = logfile

        self.sim = BlimpSim(dT)

        # Initialization section

        self.dynamics_timer = self.create_timer(dT, self.simulate_dynamics)

        self.command_subscriber = self.create_subscription(
            Quaternion,
            f"/agents/blimp{blimp_id}/motion_command",
            self.command_callback,
            1
        )

        self.mocap_publisher = self.create_publisher(
            RigidBodies,
            f"/rigid_bodies",
            1
        )

        # Set an initial position and input.
        self.u = np.zeros(4) #
        self.sim.state = np.array([
            0.0, 0.0, 0.0, # vx, vy, vz
            0.0, 0.0, 0.0, # wx, wy, wz
            1.5, 0.0, 0.0, # x, y, z
            0.0, 0.0, 0.0  # phi, theta, psi
        ])

        self.get_logger().info(f'Finished initialization of RunRtaSimNode')

    def simulate_dynamics(self):
        # Simulate the dynamics of the blimp.
        self.sim.update_model(self.u)

        # Grab state from the simulator.
        state = self.sim.get_state().reshape(12,)
        # self.get_logger().info(f'{state.shape}')
        # state_dot = self.sim.get_state_dot()

        # Convert the last three elements of the state to a quaternion.
        q = euler2quat(state[9:12])

        # Package state into a RigidBodies message.
        msg = RigidBodies()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'map'
        msg.rigidbodies = [
            RigidBody(
                rigid_body_name='blimp',
                pose=Pose(
                    position=Point(x=state[6], y=state[7], z=state[8]),
                    orientation=Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
                ),
            )
        ]

        self.mocap_publisher.publish(msg)

    def command_callback(self, msg):
        # Extract the command from the message
        self.u = np.array([msg.x, msg.y, msg.z, msg.w])

    def destroy_node(self):
        print("Logging to logs/" + self.logfile)
        logger = BlimpLogger(self.logfile)
        logger.log(self.sim, None) # ctrl

def main(args=sys.argv):
    print('Simulator node for RTA')

    if len(args) < 2:
        print("Please run with log file name as argument.")
        sys.exit(0)

    rclpy.init(args=args)
    node = RunRtaSimNode(args[1],0.001)
    try:
        rclpy.spin(node)

    finally:
        node.destroy_node()

if __name__ == '__main__':
    main()
