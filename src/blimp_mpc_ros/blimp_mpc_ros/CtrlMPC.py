import gurobipy as gp
from gurobipy import GRB
import numpy as np
import time
from . CtrlFBL import CtrlFBL
from . BlimpController import BlimpController
from . BlimpSim import BlimpSim
from . utilities import *
from mistgen.mist import mist_generator 

class CtrlMPC(BlimpController):

    def __init__(self, dT, rta_dT, rta_horizon=100): #20):
        super().__init__(dT)
        
        self.metadata = np.array([
            f"dT = {dT}",
            f"rta_dT = {rta_dT}"
        ])

        self.rta_dT = rta_dT
        self.rta_horizon = rta_horizon
        self.horizon = int(rta_dT / dT * rta_horizon)

        self.k1 = np.array([0.3, 0.3, 5, 0.2]).reshape((4,1))
        self.k2 = np.array([0.1, 0.1, 1, 0.3]).reshape((4,1))

    # TODO: we have two horizons: one for the RTA and one for the MPC.
    # MPC horizon = (rta_dT / dT) * RTA horizon. Clarify this!
    def setup_optimization_program(self, sim):
        # Construct a Gurobi model to generate control actions
        self.model = gp.Model("blimp_mpc")
        self.q = self.model.addMVar((4, self.horizon-1), lb=-GRB.INFINITY, name="q")
        self.x = self.model.addMVar((8, self.horizon), lb=-GRB.INFINITY, name="x")
        # the eight states are:
        # [vx, x, vy, y, vz, z, wpsi, psi]^T
        # the four inputs are:
        # [f_x, f_y, f_z, tau_z]^T, I think.
        self.j = 0 # RTA current time step.
        # The prediction horizon is given.
        x0 = self.get_state(sim) # To get the initial state.
        # Use a discrete-time double integrator model for the blimp.
        
        A1 = np.array([[1, 0],
                       [self.rta_dT, 1]])
        B1 = np.array([[0],
                       [self.rta_dT]])
        
        # Create a block matrix for the state-space model, first with 8 state variables.
        Ab = np.block([[A1, np.zeros((2, 6))],
                      [np.zeros((2, 2)), A1, np.zeros((2, 4))],
                      [np.zeros((2, 4)), A1, np.zeros((2, 2))],
                      [np.zeros((2, 6)), A1]])
        Bb = np.block([[B1, np.zeros((2, 3))],
                       [np.zeros((2, 1)), B1, np.zeros((2, 2))],
                       [np.zeros((2, 2)), B1, np.zeros((2, 1))],
                       [np.zeros((2, 3)), B1]])
        
        # Permute the rows so that we have the position states first.
        print(Ab)
        Ab = Ab[[1,3,5,7,0,2,4,6],:]
        Bb = Bb[[1,3,5,7,0,2,4,6],:]
        # Now we have for states [x,y,z,psi,vx,vy,vz,wpsi]^T and inputs [fx,fy,fz,tauz]^T.

        print('[INFO] Ab shape:', Ab.shape)
        print('[INFO] Bb shape:', Bb.shape)
        self.add_system_dynamics(Ab, Bb, self.horizon)
        self.x0_condition = None # pre-allocate.
        self.set_initial_condition(x0)
        self.add_control_constraints(None) # TODO: define the input constraint set.

    def add_control_constraints(self, q_polytope):
        # Add constraints to self.q
        for i in range(self.horizon-1):
            # self.model.addConstr(q_polytope.P @ self.q[:,i] >= q_polytope.p)
            self.model.addConstr(self.q[:,i] <= .05) # TODO: remove.
            self.model.addConstr(self.q[:,i] >= -.05)
    
    def set_initial_condition(self, x0):
        if self.x0_condition is not None:
            self.model.remove(self.x0_condition)

        self.x0_condition = self.model.addConstr(self.x[:,0] == x0[[0,1,2,5,6,7,8,11],0])

    def add_system_dynamics(self, A, B, horizon):
        # Recursively add the system dynamics to the optimization program
        for i in range(horizon-1):
            self.model.addConstr(self.x[:,i+1] == A @ self.x[:,i] + B @ self.q[:,i])
    
    def set_cost(self, rta_trajectory):
        # Set the cost to the two-norm between the predicted state and the desired state.
        cost = 0
        for i in range(self.rta_horizon):
            # i indexes the rta program.
            j = self.get_closest_true_index(i) # indexes true time
            cost += (self.x[:,j] - rta_trajectory[:, i])@(self.x[:,j] - rta_trajectory[:, i]) # TODO: define the desired state.
        
        self.cost = cost
    
    def set_cost_from_interpolation(self, interpolated_trajectory):
        cost = 0
        for i in range(self.horizon):
            # cost += (self.x[:4,i] - interpolated_trajectory[:, i])@W@(self.x[:4,i] - interpolated_trajectory[:, i])
            cost += (self.x[0,i]-interpolated_trajectory[0,i])*(self.x[0,i]-interpolated_trajectory[0,i])
            cost += (self.x[1,i]-interpolated_trajectory[1,i])*(self.x[1,i]-interpolated_trajectory[1,i])
            cost += (self.x[2,i]-interpolated_trajectory[2,i])*(self.x[2,i]-interpolated_trajectory[2,i])
            cost += (self.x[3,i]-interpolated_trajectory[3,i])*(self.x[3,i]-interpolated_trajectory[3,i])*10000
            
            # cost += self.x[3,i]@self.x[3,i] # penalize yaw


        self.cost = cost

    def solve_optimization_program(self, sim):
        # Update the optimization program with the new safe trajectory from an RTA
        # Essentially, sim.get_current_timestep() gets the true time, and j gets the "time" for the RTA.
        self.j = 0 # Update j.
        x0 = self.get_state(sim)
        self.set_initial_condition(x0)
        # Solve the optimization program.
        now = time.time()
        self.model.setObjective(self.cost, GRB.MINIMIZE)
        self.solution = self.model.optimize()
        print(f'[INFO] Optimization time: {time.time() - now} s')

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

        # Extract state variables
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

        x_dot = sim.get_var_dot('x')
        y_dot = sim.get_var_dot('y')
        z_dot = sim.get_var_dot('z')

        phi_dot = sim.get_var_dot('psi')
        theta_dot = sim.get_var_dot('theta')
        psi_dot = sim.get_var_dot('psi')

        ## Feedback-linearized tracking controller

        A = np.array([[v_y__b*(- np.cos(phi)*np.cos(psi)*psi_dot + np.sin(phi)*np.sin(psi)*phi_dot + ((np.cos(phi)*np.sin(psi) - np.cos(psi)*np.sin(phi)*np.sin(theta))*(D_vxy__CB*I_x + m_RB*m_z*r_z_gb__b*v_z__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2) + np.cos(phi)*np.cos(psi)*np.sin(theta)*phi_dot + np.cos(psi)*np.cos(theta)*np.sin(phi)*theta_dot - np.sin(phi)*np.sin(psi)*np.sin(theta)*psi_dot) + w_z__b*(((I_x*(m_x*v_x__b + m_RB*r_z_gb__b*w_y__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2) - (m_RB*r_z_gb__b*(I_y*w_y__b + m_RB*r_z_gb__b*v_x__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2))*(np.cos(phi)*np.sin(psi) - np.cos(psi)*np.sin(phi)*np.sin(theta)) + np.cos(psi)*np.cos(theta)*((I_y*(m_y*v_y__b - m_RB*r_z_gb__b*w_x__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2) + (m_RB*r_z_gb__b*(I_x*w_x__b - m_RB*r_z_gb__b*v_y__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2))) - v_z__b*((D_vz__CB*(np.sin(phi)*np.sin(psi) + np.cos(phi)*np.cos(psi)*np.sin(theta)))/m_z - np.cos(phi)*np.sin(psi)*phi_dot - np.cos(psi)*np.sin(phi)*psi_dot + np.cos(psi)*np.sin(phi)*np.sin(theta)*phi_dot + np.cos(phi)*np.sin(psi)*np.sin(theta)*psi_dot - np.cos(phi)*np.cos(psi)*np.cos(theta)*theta_dot + (m_RB*r_z_gb__b*(m_y*v_y__b - m_RB*r_z_gb__b*w_x__b)*(np.cos(phi)*np.sin(psi) - np.cos(psi)*np.sin(phi)*np.sin(theta)))/(I_x*m_y - m_RB**2*r_z_gb__b**2) - (m_RB*r_z_gb__b*np.cos(psi)*np.cos(theta)*(m_x*v_x__b + m_RB*r_z_gb__b*w_y__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2)) - w_x__b*(((m_y*v_y__b - m_RB*r_z_gb__b*w_x__b)*(np.sin(phi)*np.sin(psi) + np.cos(phi)*np.cos(psi)*np.sin(theta)))/m_z + ((np.cos(phi)*np.sin(psi) - np.cos(psi)*np.sin(phi)*np.sin(theta))*(I_x*m_z*v_z__b - D_omega_xy__CB*m_RB*r_z_gb__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2) + (I_z*m_RB*r_z_gb__b*np.cos(psi)*np.cos(theta)*w_z__b)/(I_y*m_x - m_RB**2*r_z_gb__b**2)) + w_y__b*(((m_x*v_x__b + m_RB*r_z_gb__b*w_y__b)*(np.sin(phi)*np.sin(psi) + np.cos(phi)*np.cos(psi)*np.sin(theta)))/m_z - (np.cos(psi)*np.cos(theta)*(I_y*m_z*v_z__b - D_omega_xy__CB*m_RB*r_z_gb__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2) + (I_z*m_RB*r_z_gb__b*w_z__b*(np.cos(phi)*np.sin(psi) - np.cos(psi)*np.sin(phi)*np.sin(theta)))/(I_x*m_y - m_RB**2*r_z_gb__b**2)) - v_x__b*(np.cos(theta)*np.sin(psi)*psi_dot + np.cos(psi)*np.sin(theta)*theta_dot + (np.cos(psi)*np.cos(theta)*(D_vxy__CB*I_y + m_RB*m_z*r_z_gb__b*v_z__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2)) + (f_g*m_RB*r_z_gb__b**2*np.cos(theta)*np.sin(phi)*(np.cos(phi)*np.sin(psi) - np.cos(psi)*np.sin(phi)*np.sin(theta)))/(I_x*m_y - m_RB**2*r_z_gb__b**2) + (f_g*m_RB*r_z_gb__b**2*np.cos(psi)*np.cos(theta)*np.sin(theta))/(I_y*m_x - m_RB**2*r_z_gb__b**2)],
                    [v_z__b*((D_vz__CB*(np.cos(psi)*np.sin(phi) - np.cos(phi)*np.sin(psi)*np.sin(theta)))/m_z - np.cos(phi)*np.cos(psi)*phi_dot + np.sin(phi)*np.sin(psi)*psi_dot + np.cos(phi)*np.cos(psi)*np.sin(theta)*psi_dot + np.cos(phi)*np.cos(theta)*np.sin(psi)*theta_dot - np.sin(phi)*np.sin(psi)*np.sin(theta)*phi_dot + (m_RB*r_z_gb__b*(m_y*v_y__b - m_RB*r_z_gb__b*w_x__b)*(np.cos(phi)*np.cos(psi) + np.sin(phi)*np.sin(psi)*np.sin(theta)))/(I_x*m_y - m_RB**2*r_z_gb__b**2) + (m_RB*r_z_gb__b*np.cos(theta)*np.sin(psi)*(m_x*v_x__b + m_RB*r_z_gb__b*w_y__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2)) - w_z__b*(((I_x*(m_x*v_x__b + m_RB*r_z_gb__b*w_y__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2) - (m_RB*r_z_gb__b*(I_y*w_y__b + m_RB*r_z_gb__b*v_x__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2))*(np.cos(phi)*np.cos(psi) + np.sin(phi)*np.sin(psi)*np.sin(theta)) - np.cos(theta)*np.sin(psi)*((I_y*(m_y*v_y__b - m_RB*r_z_gb__b*w_x__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2) + (m_RB*r_z_gb__b*(I_x*w_x__b - m_RB*r_z_gb__b*v_y__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2))) - v_y__b*(np.cos(psi)*np.sin(phi)*phi_dot + np.cos(phi)*np.sin(psi)*psi_dot + ((np.cos(phi)*np.cos(psi) + np.sin(phi)*np.sin(psi)*np.sin(theta))*(D_vxy__CB*I_x + m_RB*m_z*r_z_gb__b*v_z__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2) - np.cos(phi)*np.sin(psi)*np.sin(theta)*phi_dot - np.cos(psi)*np.sin(phi)*np.sin(theta)*psi_dot - np.cos(theta)*np.sin(phi)*np.sin(psi)*theta_dot) + w_x__b*(((m_y*v_y__b - m_RB*r_z_gb__b*w_x__b)*(np.cos(psi)*np.sin(phi) - np.cos(phi)*np.sin(psi)*np.sin(theta)))/m_z + ((np.cos(phi)*np.cos(psi) + np.sin(phi)*np.sin(psi)*np.sin(theta))*(I_x*m_z*v_z__b - D_omega_xy__CB*m_RB*r_z_gb__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2) - (I_z*m_RB*r_z_gb__b*np.cos(theta)*np.sin(psi)*w_z__b)/(I_y*m_x - m_RB**2*r_z_gb__b**2)) - w_y__b*(((m_x*v_x__b + m_RB*r_z_gb__b*w_y__b)*(np.cos(psi)*np.sin(phi) - np.cos(phi)*np.sin(psi)*np.sin(theta)))/m_z + (np.cos(theta)*np.sin(psi)*(I_y*m_z*v_z__b - D_omega_xy__CB*m_RB*r_z_gb__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2) + (I_z*m_RB*r_z_gb__b*w_z__b*(np.cos(phi)*np.cos(psi) + np.sin(phi)*np.sin(psi)*np.sin(theta)))/(I_x*m_y - m_RB**2*r_z_gb__b**2)) - v_x__b*(- np.cos(psi)*np.cos(theta)*psi_dot + np.sin(psi)*np.sin(theta)*theta_dot + (np.cos(theta)*np.sin(psi)*(D_vxy__CB*I_y + m_RB*m_z*r_z_gb__b*v_z__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2)) - (f_g*m_RB*r_z_gb__b**2*np.cos(theta)*np.sin(phi)*(np.cos(phi)*np.cos(psi) + np.sin(phi)*np.sin(psi)*np.sin(theta)))/(I_x*m_y - m_RB**2*r_z_gb__b**2) + (f_g*m_RB*r_z_gb__b**2*np.cos(theta)*np.sin(psi)*np.sin(theta))/(I_y*m_x - m_RB**2*r_z_gb__b**2)],
                    [w_x__b*((np.cos(theta)*np.sin(phi)*(I_x*m_z*v_z__b - D_omega_xy__CB*m_RB*r_z_gb__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2) - (np.cos(phi)*np.cos(theta)*(m_y*v_y__b - m_RB*r_z_gb__b*w_x__b))/m_z + (I_z*m_RB*r_z_gb__b*np.sin(theta)*w_z__b)/(I_y*m_x - m_RB**2*r_z_gb__b**2)) + w_y__b*((np.sin(theta)*(I_y*m_z*v_z__b - D_omega_xy__CB*m_RB*r_z_gb__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2) + (np.cos(phi)*np.cos(theta)*(m_x*v_x__b + m_RB*r_z_gb__b*w_y__b))/m_z - (I_z*m_RB*r_z_gb__b*np.cos(theta)*np.sin(phi)*w_z__b)/(I_x*m_y - m_RB**2*r_z_gb__b**2)) - v_x__b*(np.cos(theta)*theta_dot - (np.sin(theta)*(D_vxy__CB*I_y + m_RB*m_z*r_z_gb__b*v_z__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2)) - w_z__b*(np.cos(theta)*np.sin(phi)*((I_x*(m_x*v_x__b + m_RB*r_z_gb__b*w_y__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2) - (m_RB*r_z_gb__b*(I_y*w_y__b + m_RB*r_z_gb__b*v_x__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2)) + (np.sin(theta)*(I_y*m_y*v_y__b - m_RB**2*r_z_gb__b**2*v_y__b + I_x*m_RB*r_z_gb__b*w_x__b - I_y*m_RB*r_z_gb__b*w_x__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2)) - v_z__b*(np.cos(theta)*np.sin(phi)*phi_dot + np.cos(phi)*np.sin(theta)*theta_dot + (D_vz__CB*np.cos(phi)*np.cos(theta))/m_z + (m_RB*r_z_gb__b*np.sin(theta)*(m_x*v_x__b + m_RB*r_z_gb__b*w_y__b))/(I_y*m_x - m_RB**2*r_z_gb__b**2) - (m_RB*r_z_gb__b*np.cos(theta)*np.sin(phi)*(m_y*v_y__b - m_RB*r_z_gb__b*w_x__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2)) - v_y__b*(- np.cos(phi)*np.cos(theta)*phi_dot + np.sin(phi)*np.sin(theta)*theta_dot + (np.cos(theta)*np.sin(phi)*(D_vxy__CB*I_x + m_RB*m_z*r_z_gb__b*v_z__b))/(I_x*m_y - m_RB**2*r_z_gb__b**2)) - (f_g*m_RB*r_z_gb__b**2*np.sin(theta)**2)/(I_y*m_x - m_RB**2*r_z_gb__b**2) + (f_g*m_RB*r_z_gb__b**2*np.sin(phi)**2*(np.sin(theta)**2 - 1))/(I_x*m_y - m_RB**2*r_z_gb__b**2)],
                    [w_y__b*((np.cos(phi)*phi_dot)/np.cos(theta) + (np.cos(phi)*(I_x*w_x__b - m_RB*r_z_gb__b*v_y__b))/(I_z*np.cos(theta)) - (np.sin(phi)*(D_omega_xy__CB*m_x - m_RB*m_z*r_z_gb__b*v_z__b))/(np.cos(theta)*(I_y*m_x - m_RB**2*r_z_gb__b**2)) - (np.sin(phi)*np.sin(theta)*theta_dot)/(np.sin(theta)**2 - 1)) - w_z__b*((np.sin(phi)*phi_dot)/np.cos(theta) + (D_omega_z__CB*np.cos(phi))/(I_z*np.cos(theta)) - (np.cos(phi)*np.sin(theta)*theta_dot)/np.cos(theta)**2 + (np.sin(phi)*(I_x*m_x*w_x__b - m_RB**2*r_z_gb__b**2*w_x__b - m_RB*m_x*r_z_gb__b*v_y__b + m_RB*m_y*r_z_gb__b*v_y__b))/(np.cos(theta)*(I_y*m_x - m_RB**2*r_z_gb__b**2))) - v_x__b*((np.cos(phi)*(m_y*v_y__b - m_RB*r_z_gb__b*w_x__b))/(I_z*np.cos(theta)) - (np.sin(phi)*(m_x*m_z*v_z__b + D_vxy__CB*m_RB*r_z_gb__b))/(np.cos(theta)*(I_y*m_x - m_RB**2*r_z_gb__b**2))) - w_x__b*((np.cos(phi)*(I_y*w_y__b + m_RB*r_z_gb__b*v_x__b))/(I_z*np.cos(theta)) - (I_z*m_x*np.sin(phi)*w_z__b)/(np.cos(theta)*(I_y*m_x - m_RB**2*r_z_gb__b**2))) + (np.cos(phi)*v_y__b*(m_x*v_x__b + m_RB*r_z_gb__b*w_y__b))/(I_z*np.cos(theta)) - (m_x*np.sin(phi)*v_z__b*(m_x*v_x__b + m_RB*r_z_gb__b*w_y__b))/(np.cos(theta)*(I_y*m_x - m_RB**2*r_z_gb__b**2)) - (f_g*m_x*r_z_gb__b*np.sin(phi)*np.sin(theta))/(np.cos(theta)*(I_y*m_x - m_RB**2*r_z_gb__b**2))]
                    ])
        
        Binv = np.array([[(np.cos(psi)*np.cos(theta)*(I_y*m_x - m_RB**2*r_z_gb__b**2))/(I_y - m_RB*r_z_gb__b*r_z_tg__b), (np.cos(theta)*np.sin(psi)*(I_y*m_x - m_RB**2*r_z_gb__b**2))/(I_y - m_RB*r_z_gb__b*r_z_tg__b), -(np.sin(theta)*(I_y*m_x - m_RB**2*r_z_gb__b**2))/(I_y - m_RB*r_z_gb__b*r_z_tg__b), 0],
                        [-((I_x*m_y - m_RB**2*r_z_gb__b**2)*(np.cos(phi)*np.sin(psi) - np.cos(psi)*np.sin(phi)*np.sin(theta)))/(I_x - m_RB*r_z_gb__b*r_z_tg__b), ((I_x*m_y - m_RB**2*r_z_gb__b**2)*(np.cos(phi)*np.cos(psi) + np.sin(phi)*np.sin(psi)*np.sin(theta)))/(I_x - m_RB*r_z_gb__b*r_z_tg__b), (np.cos(theta)*np.sin(phi)*(I_x*m_y - m_RB**2*r_z_gb__b**2))/(I_x - m_RB*r_z_gb__b*r_z_tg__b), 0],
                        [m_z*np.sin(phi)*np.sin(psi) + m_z*np.cos(phi)*np.cos(psi)*np.sin(theta), m_z*np.cos(phi)*np.sin(psi)*np.sin(theta) - m_z*np.cos(psi)*np.sin(phi), m_z*np.cos(phi)*np.cos(theta), 0],
                        [(I_z*np.cos(psi)*np.cos(theta)*np.sin(phi)*(m_RB*r_z_gb__b - m_x*r_z_tg__b))/(np.cos(phi)*(I_y - m_RB*r_z_gb__b*r_z_tg__b)), (I_z*np.cos(theta)*np.sin(phi)*np.sin(psi)*(m_RB*r_z_gb__b - m_x*r_z_tg__b))/(np.cos(phi)*(I_y - m_RB*r_z_gb__b*r_z_tg__b)), -(I_z*np.sin(phi)*np.sin(theta)*(m_RB*r_z_gb__b - m_x*r_z_tg__b))/(np.cos(phi)*(I_y - m_RB*r_z_gb__b*r_z_tg__b)), (I_z*np.cos(theta))/np.cos(phi)]
                        ])

        # # Instead, get q from the optimization program
        # if self.q.X.shape[1] <= self.j: #<= self.j: # commented code should be correct.
        #     print('[WARN] Computing a new control action.')
        #     # trajectory = self.get_rta_trajectory(n)
        #     # self.set_cost(trajectory)
            # self.compute_interpolated_trajectory(n)
        if self.rta_trajectory_updated: # Time to re-compute the trajectory
            state = self.get_state(sim)

            # self.calculate_nominal_trajectory(n)
            # sim.current_timestep = 0

            # self.compute_interpolated_trajectory(n, state) # instead of the previous two functions.
            self.compute_zero_order_hold_trajectory(n, state)
            self.rta_trajectory_updated = False
        #     self.solve_optimization_program(sim)
        # q = self.q.X[:,self.j:self.j+1] # Get the control action from the optimization program.
        # self.j += 1

        # u = Binv @ (q - A)

        # sim.end_timer()
        
        # return u.reshape((4,1))

        zeta1 = np.array([[x],
                          [y],
                          [z],
                          [psi]])
        zeta2 = np.array([[x_dot],
                          [y_dot],
                          [z_dot],
                          [psi_dot]])

        yd = np.array([[self.traj_x[n]],
                       [self.traj_y[n]],
                       [self.traj_z[n]],
                       [self.traj_psi[n]]])
        yd_dot = np.array([[self.traj_x_dot[n]],
                           [self.traj_y_dot[n]],
                           [self.traj_z_dot[n]],
                           [self.traj_psi_dot[n]]])
        yd_ddot = np.array([[self.traj_x_ddot[n]],
                            [self.traj_y_ddot[n]],
                            [self.traj_z_ddot[n]],
                            [self.traj_psi_ddot[n]]])
        if hasattr(self, 'traj_u_x'):
            u_ff = np.array([[self.traj_u_x[n]],
                             [self.traj_u_y[n]],
                             [self.traj_u_z[n]],
                             [self.traj_u_psi[n]]])
        else:
            u_ff = np.zeros((4,1))
        
        e1 = zeta1 - yd
        e2 = zeta2 - yd_dot

        # TODO: test where u_ff goes. It is either added to q or k_x. 
        q = -self.k1 * e1.reshape((4,1)) - self.k2 * e2.reshape((4,1))# + yd_ddot
        # + u_ff
        
        k_x = Binv @ (q - A) + u_ff

        print(f'Norm of feed forward term: {np.linalg.norm(u_ff, axis=1)}')
        print(f'Norm of feedback term: {np.linalg.norm(k_x, axis=1)}')

        # Extract the yaw input from k_x, and include that
        # k_x = u_ff + np.array([[0],[0],[0],[k_x[3,0]]])

        sim.end_timer()


        if sim.time_delta > (self.dT * .9e9):
            print(f'[WARN] Ctrl computation took {sim.time_delta} [nano]seconds')

        # Check and make sure that k_x is not None.
        print(f'State: {np.round(zeta1, 3)}') # Ensure state data is available.
        print(f'Trajectory outputs: {np.round(yd, 3)}') # Ensure trajectory information is available.
        print(f'Feedback linearized input: {np.round(q, 3)}') # Ensure this calculation is good.
        print(f'Applied input: {np.round(k_x, 3)}')
        print('[DEBUG] end get_ctrl_action debugging messages.')
        
        return k_x.reshape((4,1))

    def get_rta_trajectory(self, n):
        pass # Should be overridden by a child class.

    def calculate_nominal_trajectory(self, n): # Vanilla
        rta_trajectory = self.get_rta_trajectory(0)
        # 
        s = rta_trajectory.shape[1]
        self.traj_x = rta_trajectory[0,:]
        self.traj_y = rta_trajectory[1,:]
        self.traj_z = rta_trajectory[2,:]
        self.traj_psi = rta_trajectory[3,:]

        self.traj_x_dot = rta_trajectory[4,:]
        self.traj_y_dot = rta_trajectory[5,:]
        self.traj_z_dot = rta_trajectory[6,:]
        self.traj_psi_dot = rta_trajectory[7,:]

        self.traj_x_ddot = np.zeros(s)
        self.traj_y_ddot = np.zeros(s)
        self.traj_z_ddot = np.zeros(s)
        self.traj_psi_ddot = np.zeros(s)

        self.traj_u_x = np.zeros(s)
        self.traj_u_y = np.zeros(s)
        self.traj_u_z = np.zeros(s)
        self.traj_u_psi = np.zeros(s)

    def compute_zero_order_hold_trajectory(self, n, state=None):
        rta_trajectory, u_sequence = self.get_rta_trajectory(0)

        # Given dT, rta_dT, u_sequence, and the blimp model, we can compute a series
        # of states to track. Start at the current state.

        relation = int(self.rta_dT / self.dT)
        u_zoh = np.zeros((u_sequence.shape[0], u_sequence.shape[1] * relation))
        for i in range(u_sequence.shape[1]):
            u_zoh[:,i*relation:(i+1)*relation] = u_sequence[:,i].reshape((4,1))

        x = np.zeros((12, rta_trajectory.shape[1] * relation)) # The number of predicted states.
        x[:,0] = state[[6,7,8,9,10,11,0,1,2,3,4,5],0] # (nu, eta)
        for i in range(1, x.shape[1]):
            # Use the numpy blimp model
            x[:,i] = x[:,i-1] + self.dT*BlimpSim.f_np(x[:,i-1],u_zoh[:,i-1])
        
        self.traj_x = np.hstack((self.traj_x[:n], x[6,1:]))
        self.traj_y = np.hstack((self.traj_y[:n], x[7,1:]))
        self.traj_z = np.hstack((self.traj_z[:n], x[8,1:]))
        self.traj_psi = np.hstack((self.traj_psi[:n], x[11,1:]))

        self.traj_x_dot = np.hstack((self.traj_x_dot[:n], x[0,1:]))
        self.traj_y_dot = np.hstack((self.traj_y_dot[:n], x[1,1:]))
        self.traj_z_dot = np.hstack((self.traj_z_dot[:n], x[2,1:]))
        self.traj_psi_dot = np.hstack((self.traj_psi_dot[:n], x[5,1:]))

        self.traj_x_ddot = np.hstack((self.traj_x_ddot[:n], np.zeros(x[0,1:].shape)))
        self.traj_y_ddot = np.hstack((self.traj_y_ddot[:n], np.zeros(x[0,1:].shape)))
        self.traj_z_ddot = np.hstack((self.traj_z_ddot[:n], np.zeros(x[0,1:].shape)))
        self.traj_psi_ddot = np.hstack((self.traj_psi_ddot[:n], np.zeros(x[0,1:].shape)))

        self.traj_u_x = np.hstack((self.traj_u_x[:n], u_zoh[0,:]))
        self.traj_u_y = np.hstack((self.traj_u_y[:n], u_zoh[1,:]))
        self.traj_u_z = np.hstack((self.traj_u_z[:n], u_zoh[2,:]))
        self.traj_u_psi = np.hstack((self.traj_u_psi[:n], u_zoh[3,:]))

    def compute_interpolated_trajectory(self, n, state=None):
        # n is the current true time index.
        print("aye")
        rta_trajectory = self.get_rta_trajectory(0)
        print("bee")
        polynominal_order = 5

        max_waypoints_for_synthesis = min(self.rta_horizon, polynominal_order+1) #5 # rta_trajectory.shape[1] # Due to computation constraints.
        print("cee")
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

            v0 = rta_trajectory[4:7,0]
            # a0 = np.array([0,0,0])
            # v0 = state[6:9,0] # Current Velocities
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