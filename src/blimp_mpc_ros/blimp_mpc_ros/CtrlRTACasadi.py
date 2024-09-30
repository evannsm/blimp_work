import gurobipy as gp
from gurobipy import GRB
import numpy as np
import time
from . CtrlFBL import CtrlFBL
from . BlimpController import BlimpController
from . BlimpSim import BlimpSim
from . utilities import *
from mistgen.mist import mist_generator 
import casadi

class CtrlRTACasadi(BlimpController):

    def __init__(self, dT, rta_dT, rta_horizon=100): #20):
        super().__init__(dT)
        
        self.rta_dT = rta_dT
        self.rta_horizon = rta_horizon
        self.horizon = int(rta_dT / dT * rta_horizon)

        max_vx_err = 0.1
        max_vy_err = 0.1
        max_vz_err = 0.1
        
        max_wx_err = 10
        max_wy_err = 10
        max_wz_err = 5
        
        max_x_err = 0.05
        max_y_err = 0.05
        max_z_err = 0.05
        
        max_phi_err = 10 * np.pi/180
        max_th_err = 10 * np.pi/180
        max_psi_err = 10 * np.pi/180
        
        # Define in an 8x8 matrix without pitch and roll
        self.Q = np.array([
            [1/(max_vx_err**2), 0, 0, 0, 0, 0, 0, 0],       # vx
            [0, 1/(max_vy_err**2), 0, 0, 0, 0, 0, 0],       # vy
            [0, 0, 1/(max_vz_err**2), 0, 0, 0, 0, 0],       # vz
            [0, 0, 0, 1/(max_wz_err**2), 0, 0, 0, 0],       # wz
            [0, 0, 0, 0, 1/(max_x_err**2), 0, 0, 0],       # x
            [0, 0, 0, 0, 0, 1/(max_y_err**2), 0, 0],       # y
            [0, 0, 0, 0, 0, 0, 1/(max_z_err**2), 0],       # z
            [0, 0, 0, 0, 0, 0, 0, 10/(max_psi_err**2)],       # psi
        ])
        
        max_fx = 0.035
        max_fy = 0.035
        max_fz = 0.2
        max_tz = 0.001
        
        self.R = np.array([
        	[1/(max_fx**2), 0, 0, 0],
        	[0, 1/(max_fy**2), 0, 0],
        	[0, 0, 1/(max_fz**2), 0],
        	[0, 0, 0, 1/(max_tz**2)]
        ]) * 1 #* 100

        # Setup controller.
        N = 15 # MPC horizon length

        self.opti = casadi.Opti()
        self.opt_u = self.opti.variable(4, N)
        self.opt_x = self.opti.variable(12, N+1)

        # u_ref = self.opti.parameter(N, 4)
        self.y_ref = self.opti.parameter(8, N) # In the output space.
        self.opt_x_t = self.opti.parameter(12,) # Initialization

        opts_setting = {
            'ipopt.max_iter': 2000
        }
        
        self.opti.solver('ipopt', opts_setting)

        # Initial condition.
        self.opti.subject_to( self.opt_x[:,0] == self.opt_x_t )

        # Create the dynamics equality constraints
        for j in range(N):
            x_next = self.opt_x[:, j] + dT * BlimpSim.f(self.opt_x[:, j], self.opt_u[:, j])
            self.opti.subject_to( self.opt_x[:, j+1] == x_next )

        # Create the cost function.
        obj = 0
        gamma = .1 # Weighting on the control effort.
        for i in range(N):
            state_error = self.opt_x[[0,1,2,5,6,7,8,11], i+1] - self.y_ref[:, i]
            obj += casadi.mtimes([state_error.T, self.Q, state_error])
            # Penalize the control effort.
            obj += gamma * casadi.mtimes([self.opt_u[:, i].T, self.R, self.opt_u[:, i]])
        
        self.opti.minimize(obj)

        # Bound the control input variables.
        self.opti.subject_to( self.opti.bounded(-max_fx, self.opt_u[0, :], max_fx) )
        self.opti.subject_to( self.opti.bounded(-max_fy, self.opt_u[1, :], max_fy) )
        self.opti.subject_to( self.opti.bounded(-max_fz, self.opt_u[2, :], max_fz) )
        self.opti.subject_to( self.opti.bounded(-max_tz, self.opt_u[3, :], max_tz) )
        
        self.metadata = np.array([
            str(self.Q),
            str(self.R),
            str(N)
        ])

        self.N = N

    def get_closest_true_index(self, i):
        # Given j \in \{0, ..., self.horizon\}, find the closest index in time.
        return int(i * self.rta_dT / self.dT)

    def get_state(self, sim):
        # Returns the current state in R^12
        x = sim.get_var('x')
        y = sim.get_var('y')
        z = sim.get_var('z')

        phi = sim.get_var('phi')
        theta = sim.get_var('theta')
        psi = sim.get_var('psi')
        
        v_x__b = sim.get_var('vx')
        v_y__b = sim.get_var('vy')
        v_z__b = sim.get_var('vz')

        w_x__b = sim.get_var('wx')
        w_y__b = sim.get_var('wy')
        w_z__b = sim.get_var('wz')

        return np.array([x, y, z, phi, theta, psi,
                         v_x__b, v_y__b, v_z__b, w_x__b, w_y__b, w_z__b]).reshape((12,1))

    def get_ctrl_action(self, sim : BlimpSim): 
        sim.start_timer()
        
        n = sim.get_current_timestep() # In true time.
        
        if n >= len(self.traj_x):
            print(f'[WARN] at the end of the simulation!')
            return None # At the end of the simulation.

        if self.rta_trajectory_updated: # Time to re-compute the trajectory
            state = self.get_state(sim)
            self.compute_interpolated_trajectory(n, state) # instead of the previous two functions.
            self.rta_trajectory_updated = False
 
        traj_ref = np.vstack((
            self.traj_x_dot[n:n+self.N],
            self.traj_y_dot[n:n+self.N],
            self.traj_z_dot[n:n+self.N],
            self.traj_psi_dot[n:n+self.N],
            self.traj_x[n:n+self.N],
            self.traj_y[n:n+self.N],
            self.traj_z[n:n+self.N],
            self.traj_psi[n:n+self.N],
        ))

        print('[INFO] made it to set_value for the reference trajectory')
        self.opti.set_value(self.y_ref, traj_ref)

        # Stack sim.get_var('x') to sim.get_var('psi') to get the current state.
        x_t = np.array([
            sim.get_var('vx'),
            sim.get_var('vy'),
            sim.get_var('vz'),
            sim.get_var('wx'),
            sim.get_var('wy'),
            sim.get_var('wz'),
            sim.get_var('x'),
            sim.get_var('y'),
            sim.get_var('z'),
            sim.get_var('phi'),
            sim.get_var('theta'),
            sim.get_var('psi')
        ])

        # set_initial provides an initial guess, NOT an initial condition!
        # self.opti.set_initial(self.opt_x, x_t)
        self.opti.set_value(self.opt_x_t, x_t.reshape((1,12)))

        solution = self.opti.solve()

        u = solution.value(self.opt_u[:, 0])
        
        sim.end_timer()

        return u.reshape((4,1))

    def get_rta_trajectory(self, n):
        pass # Should be overridden by a child class.

    def compute_interpolated_trajectory(self, n, state=None):
        # n is the current true time index.

        rta_trajectory, u_sequence = self.get_rta_trajectory(0)

        polynominal_order = 5

        max_waypoints_for_synthesis = min(self.rta_horizon, polynominal_order+1) #5 # rta_trajectory.shape[1] # Due to computation constraints.

        myMistGen = mist_generator(interval=self.dT, n_order=polynominal_order, n_deri=4) # minimum accel, jerk, or snap?

        if n <= 1:
            # Do something special to initialize
            v0 = np.zeros((3,))
            a0 = np.zeros((3,))
            ve = np.zeros((3,))
            ae = np.zeros((3,))
            waypts = rta_trajectory[0:3, :max_waypoints_for_synthesis]
        elif True:
            # Initialize the rta_trajectory with the current state.

            # v0 = rta_trajectory[4:7,0]
            # a0 = np.array([0,0,0])
            v0 = state[6:9,0] # Current Velocities
            # a0 = np.array([self.traj_x_ddot[n-1], self.traj_y_ddot[n-1], self.traj_z_ddot[n-1]]) # Last tracked acceleration
            a0 = np.zeros((3,))
            ve = rta_trajectory[4:7,min(max_waypoints_for_synthesis-1, self.rta_horizon-1)] # Final Velocity
            ae = np.zeros((3,)) # Final Acceleration. Assume for now that the RTA does not compute a final acceleration.

            # recall: rta_trajectory is a vector in R^{8\times N}

            # Pre-append waypts with the current state.
            waypts = rta_trajectory[0:3, :max_waypoints_for_synthesis]
            
            # TODO update 071724: the RTA now is pre-appended with the first predicted state,
            # relative to the previous rta time step. So, don't include the state.
            v0 = rta_trajectory[4:7, 0]
            # The other option is to replace the previous trajectory waypoint with the current state.

            # waypts = np.hstack((state[:3,:], waypts)) # Careful of conventions between waypts and the trajectory computed by the rta.

            # Discard inputs beyond max_waypoints_for_synthesis
            u_sequence = u_sequence[:,:max_waypoints_for_synthesis]

        else:
            # Select the historical index that corresponds to a real prescribed output trajectory

            # Initialize the waypoints with the previous rta_trajectory solution
            v0 = np.array([self.traj_x_dot[n-1], self.traj_y_dot[n-1], self.traj_z_dot[n-1]])
            a0 = np.zeros((3,))
            ve = rta_trajectory[4:7, min(max_waypoints_for_synthesis, self.rta_horizon-1)]
            ae = np.zeros((3,))

            # Get the last trajectory outputs
            x_last = self.traj_x[n-1]
            y_last = self.traj_y[n-1]
            z_last = self.traj_z[n-1]

            # Create a 3x1 array of these.
            previous_waypoint = np.array([x_last, y_last, z_last]).reshape((3,1))

            waypts = rta_trajectory[0:3, :max_waypoints_for_synthesis]
            waypts = np.hstack((previous_waypoint, waypts))
            print(f'[DEBUG] waypts: {waypts}')

        try:
            xxs, yys, zzs, xx_v_s, yy_v_s, zz_v_s, xx_a_s, yy_a_s, zz_a_s, tts = myMistGen.mist_3d_gen(waypts, v0, a0,
                                            ve, ae, self.rta_dT * rta_trajectory.shape[1], do_vel=True, do_acc=True)

        except:
            print('[ERROR] Failed to interpolate a valid trajectory!')
            return

        relation = int(self.rta_dT / self.dT)
        u_zoh = np.zeros((u_sequence.shape[0], u_sequence.shape[1] * relation))
        for i in range(u_sequence.shape[1]):
            u_zoh[:,i*relation:(i+1)*relation] = u_sequence[:,i].reshape((4,1))

        # Create a vector of zeros with the same shape as xxs, for the target yaw of zero degrees.
        psi_s = np.zeros(xxs.shape)

        # Setup trajectory.
        # print(f'[DEBUG] self.traj_x.shape = {self.traj_x.shape}')
        # print(f'[DEBUG] xxs.shape = {xxs.shape}')
        # print(f'[DEBUG] current time step = {n}')
        if n <= 1:
            self.traj_x = xxs
            self.traj_y = yys
            self.traj_z = zzs
            self.traj_psi = psi_s

            self.traj_x_dot = xx_v_s
            self.traj_y_dot = yy_v_s
            self.traj_z_dot = zz_v_s
            self.traj_psi_dot = np.zeros(psi_s.shape)

            self.traj_x_ddot = xx_a_s
            self.traj_y_ddot = yy_a_s
            self.traj_z_ddot = zz_a_s
            self.traj_psi_ddot = np.zeros(psi_s.shape)
            
            self.traj_u_x = np.zeros(xxs.shape)
            self.traj_u_y = np.zeros(xxs.shape)
            self.traj_u_z = np.zeros(xxs.shape)
            self.traj_u_psi = np.zeros(xxs.shape)
        else:
            self.traj_x = np.hstack((self.traj_x[:n], xxs[1:]))
            self.traj_y = np.hstack((self.traj_y[:n], yys[1:]))
            self.traj_z = np.hstack((self.traj_z[:n], zzs[1:]))
            self.traj_psi = np.hstack((self.traj_psi[:n], psi_s[1:]))

            self.traj_x_dot = np.hstack((self.traj_x_dot[:n], xx_v_s[1:]))
            self.traj_y_dot = np.hstack((self.traj_y_dot[:n], yy_v_s[1:]))
            self.traj_z_dot = np.hstack((self.traj_z_dot[:n], zz_v_s[1:]))
            self.traj_psi_dot = np.hstack((self.traj_psi_dot[:n], np.zeros(psi_s[1:].shape)))

            self.traj_x_ddot = np.hstack((self.traj_x_ddot[:n], xx_a_s[1:]))
            self.traj_y_ddot = np.hstack((self.traj_y_ddot[:n], yy_a_s[1:]))
            self.traj_z_ddot = np.hstack((self.traj_z_ddot[:n], zz_a_s[1:]))
            self.traj_psi_ddot = np.hstack((self.traj_psi_ddot[:n], np.zeros(psi_s[1:].shape)))

            self.traj_u_x = np.hstack((self.traj_u_x[:n], u_zoh[0,:]))
            self.traj_u_y = np.hstack((self.traj_u_y[:n], u_zoh[1,:]))
            self.traj_u_z = np.hstack((self.traj_u_z[:n], u_zoh[2,:]))
            self.traj_u_psi = np.hstack((self.traj_u_psi[:n], u_zoh[3,:]))

        # Output the last x values.
        print(f'[DEBUG] The projected values of x are: {np.round(self.traj_x[n-1:], 3)}')
        print(f'[DEBUG] The projected values of v_x are: {np.round(self.traj_x_dot[n-1:], 3)}')
        print(f'[DEBUG] The projected values of \ddot{{x}} are {np.round(self.traj_x_ddot[n-1:], 3)}')
        print(f'[DEBUG] The projected values of u_x are {np.round(self.traj_u_x[n-1:], 3)}')