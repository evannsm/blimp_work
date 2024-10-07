import numpy as np
import csv

class BlimpController():

    def __init__(self, dT, skip_derivatives=False):
        self.dT = dT
        self.error_history = None
        self.is_initialized = False

        self.rta_trajectory_updated = False

        self.traj_x = None
        self.traj_y = None
        self.traj_z = None
        self.traj_psi = None
        
        self.metadata = None

        self.order = 12
        self.num_inputs = 4
        self.num_outputs = 6
        self.cbf_history = np.array([0]).reshape(-1,1)
        
    def init_trajectory(self, trajectory):
        self.traj_x         = trajectory[0]
        self.traj_y         = trajectory[1]
        self.traj_z         = trajectory[2]
        self.traj_psi       = trajectory[3]
        
        self.traj_x_dot     = trajectory[4]
        self.traj_y_dot     = trajectory[5]
        self.traj_z_dot     = trajectory[6]
        self.traj_psi_dot   = trajectory[7]
        
        # Check that trajectory[8] exists.
        if len(trajectory) > 8:
            self.traj_x_ddot    = trajectory[8]
            self.traj_y_ddot    = trajectory[9]
            self.traj_z_ddot    = trajectory[10]
            self.traj_psi_ddot  = trajectory[11]
        else:
            print('[WARN] No trajectory second derivatives provided.')
    
    def update_rta_trajectory(self, rta_trajectory):
        self.rta_horizon       = rta_trajectory[0].shape[0]

        self.rta_traj_x        = rta_trajectory[0]
        self.rta_traj_y        = rta_trajectory[1]
        self.rta_traj_z        = rta_trajectory[2]
        self.rta_traj_psi      = rta_trajectory[3]

        self.rta_traj_x_dot    = rta_trajectory[4]
        self.rta_traj_y_dot    = rta_trajectory[5]
        self.rta_traj_z_dot    = rta_trajectory[6]
        self.rta_traj_psi_dot  = rta_trajectory[7]

        if len(rta_trajectory) > 8: # feed foward inputs provided too
            self.rta_u_x       = rta_trajectory[8]
            self.rta_u_y       = rta_trajectory[9]
            self.rta_u_z       = rta_trajectory[10]
            self.rta_u_psi     = rta_trajectory[11]

        self.rta_trajectory_updated = True # 
        
    def get_ctrl_action(self, sim):
        pass

    def init_sim(self, sim):
        pass

    def get_trajectory(self):
        return np.array([
                self.traj_x,
                self.traj_y,
                self.traj_z,
                self.traj_psi
        ]).T
    
    def get_metadata(self):
        return self.metadata
    

    def get_cbf_data(self):
        return self.cbf_history
