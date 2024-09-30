import numpy as np
from .Trajectories import Trajectories
from .CtrlMPC import CtrlMPC

# This class (and other subclasses of CtrlMPC) will be used to
# interface with the RTA, while the superclass will execute MPC.
class CtrlMPCBox(CtrlMPC):
    def __init__(self, dT, rta_dT):
        super().__init__(dT, rta_dT)

    def init_sim(self, sim):
        x0 = sim.get_var('x')
        y0 = sim.get_var('y')
        z0 = sim.get_var('z')
        psi0 = sim.get_var('psi')

        trajectory = Trajectories.get_line(x0, y0, z0, psi0, self.dT, TRACKING_TIME=10, SETTLE_TIME=10)
        self.init_trajectory(trajectory) # The above is a placeholder trajectory.
        starting_rta_trajectory = Trajectories.get_line(x0, y0, z0, psi0, self.rta_dT, TRACKING_TIME=10, SETTLE_TIME=10)
        # self.update_rta_trajectory(starting_rta_trajectory) # Initialization, as well

        self.is_initialized = True

        self.N = trajectory[0].shape[0] # The number of sampled points in the trajectory
        # This simulates a low-frequency RTA solution. Note: the RTA does not provide
        # the second derivatives of the trajectory.

        # Initialize the optimization program.
        self.setup_optimization_program(sim)

        # trajectory = self.get_rta_trajectory(0)
        # self.set_cost(trajectory)
        self.compute_interpolated_trajectory(0) # Instead.

        # self.solve_optimization_program(sim) # Initial solution.

        # trajectory needs to be converted from a tuple to a numpy array
        # return trajectory

    def get_rta_trajectory(self, n=0):
        # Get the RTA trajectory at time index n.
        rta_trajectory = np.empty((8, self.rta_horizon))
        u_sequence = np.empty((4, self.rta_horizon))
        # For logging purposes.
        print(f'[DEBUG] in get_rta_trajectory, n={n}, rta_horizon={self.rta_horizon}')
        try:
            for i in range(self.rta_horizon):
                rta_trajectory[0, i] = self.rta_traj_x[n + i]
                rta_trajectory[1, i] = self.rta_traj_y[n + i]
                rta_trajectory[2, i] = self.rta_traj_z[n + i]
                rta_trajectory[3, i] = self.rta_traj_psi[n + i]
                rta_trajectory[4, i] = self.rta_traj_x_dot[n + i]
                rta_trajectory[5, i] = self.rta_traj_y_dot[n + i]
                rta_trajectory[6, i] = self.rta_traj_z_dot[n + i]
                rta_trajectory[7, i] = self.rta_traj_psi_dot[n + i]
            # Check if self.rta_u_x exists.
            if hasattr(self, 'rta_u_x'):
                for i in range(self.rta_horizon):
                    u_sequence[0, i] = self.rta_u_x[n + i]
                    u_sequence[1, i] = self.rta_u_y[n + i]
                    u_sequence[2, i] = self.rta_u_z[n + i]
                    u_sequence[3, i] = self.rta_u_psi[n + i]

            return rta_trajectory, u_sequence
        except AttributeError:
            print('[WARN] Zero trajectory being returned!')
            # Return a bunch of zeros
            return np.zeros((8, self.rta_horizon))
