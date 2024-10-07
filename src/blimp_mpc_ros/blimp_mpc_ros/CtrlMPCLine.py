import numpy as np
from . Trajectories import Trajectories
from . CtrlMPC import CtrlMPC

# Computes a control action for a linear trajectory in the +x direction
# Given a safe trajectory computed by an RTA at a lower frequency, this class
# follows tracks the trajectory using MPC. (Assume: dT << rta_dT)

# In the future, this class (and other subclasses of CtrlMPC) will be used to
# interface with the RTA, while the superclass will execute MPC.
class CtrlMPCLine(CtrlMPC):
    def __init__(self, dT):
        rta_dT = 0.2
        rta_horizon = int(2/rta_dT)
        super().__init__(dT, rta_dT, rta_horizon)

    def init_sim(self, sim):
        # print("HEREREERE")
        x0 = sim.get_var('x')
        y0 = sim.get_var('y')
        z0 = sim.get_var('z')
        psi0 = sim.get_var('psi')

        trajectory = Trajectories.get_line(x0, y0, z0, psi0, self.dT)
        self.init_trajectory(trajectory)
        # sim.trajectory = trajectory

        self.is_initialized = True

        self.N = trajectory[0].shape[0] # The number of sampled points in the trajectory
        # This simulates a low-frequency RTA solution. Note: the RTA does not provide
        # the second derivatives of the trajectory.

        # Initialize the optimization program.
        # print('a')
        self.setup_optimization_program(sim)

        # trajectory = self.get_rta_trajectory(0)
        # self.set_cost(trajectory)
        # print('b')
        self.compute_interpolated_trajectory(0) # Instead.
        # print('c')
        self.solve_optimization_program(sim) # Initial solution.
        # print('d')
        # trajectory needs to be converted from a tuple to a numpy array
        # return trajectory

    def get_rta_trajectory(self, n):
        # Get the RTA trajectory at time index n.
        # Starting at true index n, increment by n + int(rta_dT / dT) and
        # append the result to the trajectory.
        # The result should be a 2D numpy array with shape (rta_horizon, 8), as
        # we include the derivatives (but not the second derivatives).
        rta_trajectory = np.empty((8, self.rta_horizon))
        for i in range(self.rta_horizon):
            rta_trajectory[0, i] = self.traj_x[n + i * int(self.rta_dT / self.dT)]
            rta_trajectory[1, i] = self.traj_y[n + i * int(self.rta_dT / self.dT)]
            rta_trajectory[2, i] = self.traj_z[n + i * int(self.rta_dT / self.dT)]
            rta_trajectory[3, i] = self.traj_psi[n + i * int(self.rta_dT / self.dT)]
            rta_trajectory[4, i] = self.traj_x_dot[n + i * int(self.rta_dT / self.dT)]
            rta_trajectory[5, i] = self.traj_y_dot[n + i * int(self.rta_dT / self.dT)]
            rta_trajectory[6, i] = self.traj_z_dot[n + i * int(self.rta_dT / self.dT)]
            rta_trajectory[7, i] = self.traj_psi_dot[n + i * int(self.rta_dT / self.dT)]
        return rta_trajectory