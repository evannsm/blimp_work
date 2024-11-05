import gurobipy as gp
from gurobipy import GRB
import numpy as np
import time
from . BlimpController import BlimpController
from . Trajectories import Trajectories
from . utilities import *
import control
import sys
import math as m
import jax.numpy as jnp

from . blimp_jax import *

class CtrlWardi(BlimpController):

    def __init__(self, dT):
        # print("HIHIHIHI")
        super().__init__(dT)
        self.use_CBFs = True
        # print(f"dt = {dT}")
        # exit(0)
        self.alpha = np.array([[30, 30, 30, 20]]).T
        # self.alpha = np.array([[40, 40, 40, 40]]).T
        # self.alpha = np.array([[25,35,35,35]]).T # Speed-up parameter (maybe play with uniform alpha values rather than ones that change for each input)
        # self.u = np.array([0, 0, 0, 0]).T
        self.dT = dT
        self.last_input = 0*np.array([[0.0, 0.0, -1*0.15*9.806, 0.0]]).T

        self.metadata = np.array([
            str(self.alpha),
        ])

        C = np.zeros([4,12])
        C[0,6],C[1,7], C[2,8], C[3,11] = 1,1,1,1
        self.C = C

        C = np.zeros([4,12])
        C[0,0],C[1,1], C[2,2], C[3,8] = 1,1,1,1
        self.Cjax = C

        self.T_lookahead = 1.2

        self.cbf_history =  np.zeros((1,4))

    def normalize_angle(self, angle):
        """ Normalize the angle to the range [-pi, pi]. """
        result = m.atan2(m.sin(angle), m.cos(angle))
        # #print(f"normalize_angle: input={angle}, result={result}")
        return result
    
    def shortest_path_yaw(self, desired_yaw, current_yaw): #Calculates shortest path between two yaw angles
        """ Calculate the shortest path to the desired yaw angle. """
        desired_yaw = self.normalize_angle(desired_yaw)
        current_yaw = self.normalize_angle(current_yaw)

        delta_yaw = self.normalize_angle(desired_yaw - current_yaw)
        
        return delta_yaw

    def get_tracking_error(self, sim, n, pred):
        print(f"CURR: {[sim.get_var('x'), sim.get_var('y'), sim.get_var('z'), sim.get_var('psi')]}")
        print(f"REF: {[self.traj_x[n], self.traj_y[n], self.traj_z[n], self.traj_psi[n]]}")
        n_lookahead = int(self.T_lookahead / self.dT)
        n_plus_lookahead = n + n_lookahead
        # print(f"{n_plus_lookahead =}")
        # if n > 5:
        #     sys.exit(1)
        err_x = self.traj_x[n_plus_lookahead] - pred[0][0]
        # exit(0)
        err_y = self.traj_y[n_plus_lookahead] - pred[1][0]
        err_z = self.traj_z[n_plus_lookahead] - pred[2][0]
        err_psi = self.shortest_path_yaw(self.traj_psi[n_plus_lookahead], pred[3][0])
        return np.array([[err_x, err_y, err_z, err_psi]]).T
    
    
    def euler_integration_original(self, u, sim): # DO NOT USE -- NOT FAST ENOUGH FOR 100Hz. HERE FOR REFERENCE FOR COMPILED 0-ORDER HOLD NONLINEAR PREDICTION
        """ DO NOT USE (SLOW- not compiled in C): Predicts the system output state using a numerically integrated nonlinear model with 0-order hold. """
        

        T_lookahead = self.T_lookahead
        integration_step = 0.1
        integrations = T_lookahead / integration_step
        integrations = int(integrations)     

        curr_x = sim.get_var('x')
        curr_y = sim.get_var('y')
        curr_z = sim.get_var('z')
        curr_vx = sim.get_var('vx')
        curr_vy = sim.get_var('vy')
        curr_vz = sim.get_var('vz')
        curr_roll = sim.get_var('phi')
        curr_pitch = sim.get_var('theta')
        curr_yaw = sim.get_var('psi')
        curr_wx = sim.get_var('wx')
        curr_wy = sim.get_var('wy')
        curr_wz = sim.get_var('wz')

        # print(f"last input: {u}")
        # print(f"{curr_x = }, {curr_y = }, {curr_z = }, {curr_vx = }, {curr_vy = }, {curr_vz = }, {curr_roll = }, {curr_pitch = }, {curr_yaw = }, {curr_wx = }, {curr_wy = }, {curr_wz = }")


        # #print(f"{u = }")
        # #print(f"{u.shape = }")
        # #print("HEREREJRSKL")


        tau_B = np.array([u[0][0],
                            u[1][0],
                            u[2][0],
                            -r_z_tg__b * u[1][0],
                            r_z_tg__b * u[0][0],
                            u[3][0]]).reshape((6,1))

        nu_bn_b = np.array([curr_vx, curr_vy, curr_vz, curr_wx, curr_wy, curr_wz]).reshape((6,1))

        # Restoration torque
        fg_B = R_b__n_inv(curr_roll, curr_pitch, curr_yaw) @ fg_n
        g_CB = -np.block([[np.zeros((3, 1))],
                        [np.reshape(np.cross(r_gb__b, fg_B), (3, 1))]])

        # Update state
        eta_bn_n_dot = np.block([[R_b__n(curr_roll, curr_pitch, curr_yaw),    np.zeros((3, 3))],
                                [np.zeros((3, 3)),            T(curr_roll, curr_pitch)]]) @ nu_bn_b
        
        nu_bn_b_dot = np.reshape(-M_CB_inv @ (C(M_CB, nu_bn_b) @ nu_bn_b + \
                            D_CB @ nu_bn_b + g_CB - tau_B), (6, 1))

        xdot = eta_bn_n_dot[0][0]
        ydot = eta_bn_n_dot[1][0]
        zdot = eta_bn_n_dot[2][0]
        vxdot = nu_bn_b_dot[0][0]
        vydot = nu_bn_b_dot[1][0]
        vzdot = nu_bn_b_dot[2][0]
        rolldot = eta_bn_n_dot[3][0]
        pitchdot = eta_bn_n_dot[4][0]
        yawdot = eta_bn_n_dot[5][0]
        wxdot = nu_bn_b_dot[3][0]
        wydot = nu_bn_b_dot[4][0]
        wzdot = nu_bn_b_dot[5][0]

        cumm_change_x = 0.0
        cumm_change_y = 0.0
        cumm_change_z = 0.0
        cumm_change_vx = 0.0
        cumm_change_vy = 0.0
        cumm_change_vz = 0.0
        cumm_change_roll = 0.0
        cumm_change_pitch = 0.0
        cumm_change_yaw = 0.0
        cumm_change_wx = 0.0
        cumm_change_wy = 0.0
        cumm_change_wz = 0.0

        x = curr_x
        y = curr_y
        z = curr_z
        vx = curr_vx
        vy = curr_vy
        vz = curr_vz
        phi = curr_roll
        theta = curr_pitch
        psi = curr_yaw
        wx = curr_wx
        wy = curr_wy
        wz = curr_wz

        for _ in range(integrations):
            # TODO : cumm_change_vx/vy/vz/wx/wy/wz and their relationsips to x/y/z/roll/pitch/yaw_dot should be examined before adding them together
            change_x = (xdot+cumm_change_vx) * integration_step;
            change_y = (ydot+cumm_change_vy) * integration_step;
            change_z = (zdot+cumm_change_vz) * integration_step;
            change_vx = vxdot * integration_step;
            change_vy = vydot * integration_step;
            change_vz = vzdot * integration_step;
            change_roll = (rolldot + cumm_change_wx) * integration_step;
            change_pitch = (pitchdot + cumm_change_wy) * integration_step;
            change_yaw = (yawdot + cumm_change_wz) * integration_step;
            change_wx = wxdot * integration_step;
            change_wy = wydot * integration_step;
            change_wz = wzdot * integration_step;

            

            x = x + change_x
            y = y + change_y
            z = z + change_z
            vx = vx + change_vx
            vy = vy + change_vy
            vz = vz + change_vz
            phi = phi + change_roll
            theta = theta + change_pitch
            psi = psi + change_yaw
            wx = wx + change_wx
            wy = wy + change_wy
            wz = wz + change_wz


            nu_bn_b = np.array([vx, vy, vz, wx, wy, wz]).reshape((6,1))

            # Restoration torque
            fg_B = R_b__n_inv(phi, theta, psi) @ fg_n
            g_CB = -np.block([[np.zeros((3, 1))],
                            [np.reshape(np.cross(r_gb__b, fg_B), (3, 1))]])

            # Update state
            eta_bn_n_dot = np.block([[R_b__n(phi, theta, psi),    np.zeros((3, 3))],
                                    [np.zeros((3, 3)),            T(phi, theta)]]) @ nu_bn_b
            
            nu_bn_b_dot = np.reshape(-M_CB_inv @ (C(M_CB, nu_bn_b) @ nu_bn_b + \
                                D_CB @ nu_bn_b + g_CB - tau_B), (6, 1))

            xdot = eta_bn_n_dot[0][0]
            ydot = eta_bn_n_dot[1][0]
            zdot = eta_bn_n_dot[2][0]
            vxdot = nu_bn_b_dot[0][0]
            vydot = nu_bn_b_dot[1][0]
            vzdot = nu_bn_b_dot[2][0]
            rolldot = eta_bn_n_dot[3][0]
            pitchdot = eta_bn_n_dot[4][0]
            yawdot = eta_bn_n_dot[5][0]
            wxdot = nu_bn_b_dot[3][0]
            wydot = nu_bn_b_dot[4][0]
            wzdot = nu_bn_b_dot[5][0]

            
            cumm_change_x = cumm_change_x + change_x;
            cumm_change_y = cumm_change_y + change_y; 
            cumm_change_z = cumm_change_z + change_z; 
            cumm_change_vx = cumm_change_vx + change_vx; 
            cumm_change_vy = cumm_change_vy + change_vy; 
            cumm_change_vz = cumm_change_vz + change_vz; 
            cumm_change_roll = cumm_change_roll + change_roll; 
            cumm_change_pitch = cumm_change_pitch + change_pitch; 
            cumm_change_yaw = cumm_change_yaw + change_yaw;
            cumm_change_wx = cumm_change_wx + change_wx;
            cumm_change_wy = cumm_change_wy + change_wy;
            cumm_change_wz = cumm_change_wz + change_wz;



        x = curr_x + cumm_change_x
        y = curr_y + cumm_change_y
        z = curr_z + cumm_change_z
        
        vx = curr_vx + cumm_change_vx
        vy = curr_vy + cumm_change_vy
        vz = curr_vz + cumm_change_vz
    
        roll = curr_roll + cumm_change_roll;
        pitch = curr_pitch + cumm_change_pitch;
        yaw = curr_yaw + cumm_change_yaw;

        wx = curr_wx + cumm_change_wx
        wy = curr_wy + cumm_change_wy
        wz = curr_wz + cumm_change_wz

        eta_bn_n = np.array([x, y, z, roll, pitch, yaw]).reshape((6,1))
        nu_bn_b = np.array([vx, vy, vz, wx, wy, wz]).reshape((6,1))
        nonlin_pred = np.concatenate((nu_bn_b, eta_bn_n),axis=0)
        #print(f"{nonlin_pred = }")
        return nonlin_pred
    
    def euler_integration(self, u, sim): 
        """
        Predicts the system output state using a numerically integrated nonlinear model with 0-order hold.
        """

        T_lookahead = self.T_lookahead
        integration_step = 0.05  # Reduced for more stable integration
        integrations = int(T_lookahead / integration_step)  

        curr_x = sim.get_var('x')
        curr_y = sim.get_var('y')
        curr_z = sim.get_var('z')
        curr_vx = sim.get_var('vx')
        curr_vy = sim.get_var('vy')
        curr_vz = sim.get_var('vz')
        curr_roll = sim.get_var('phi')
        curr_pitch = sim.get_var('theta')
        curr_yaw = sim.get_var('psi')
        curr_wx = sim.get_var('wx')
        curr_wy = sim.get_var('wy')
        curr_wz = sim.get_var('wz')



        tau_B = np.array([u[0][0],
                        u[1][0],
                        u[2][0],
                        -r_z_tg__b * u[1][0],
                        r_z_tg__b * u[0][0],
                        u[3][0]]).reshape((6,1))

        nu_bn_b = np.array([curr_vx, curr_vy, curr_vz, curr_wx, curr_wy, curr_wz]).reshape((6,1))

        # Restoration torque
        fg_B = R_b__n_inv(curr_roll, curr_pitch, curr_yaw) @ fg_n
        g_CB = -np.block([[np.zeros((3, 1))],
                        [np.reshape(np.cross(r_gb__b, fg_B), (3, 1))]])

        x = curr_x
        y = curr_y
        z = curr_z
        vx = curr_vx
        vy = curr_vy
        vz = curr_vz
        roll = curr_roll
        pitch = curr_pitch
        yaw = curr_yaw
        wx = curr_wx
        wy = curr_wy
        wz = curr_wz

        for _ in range(integrations):
            # Update state derivatives
            eta_bn_n_dot = np.block([[R_b__n(roll, pitch, yaw), np.zeros((3, 3))],
                                    [np.zeros((3, 3)), T(roll, pitch)]]) @ nu_bn_b

            nu_bn_b_dot = np.reshape(-M_CB_inv @ (C(M_CB, nu_bn_b) @ nu_bn_b + 
                                D_CB @ nu_bn_b + g_CB - tau_B), (6, 1))

            xdot = eta_bn_n_dot[0][0]
            ydot = eta_bn_n_dot[1][0]
            zdot = eta_bn_n_dot[2][0]
            vxdot = nu_bn_b_dot[0][0]
            vydot = nu_bn_b_dot[1][0]
            vzdot = nu_bn_b_dot[2][0]
            rolldot = eta_bn_n_dot[3][0]
            pitchdot = eta_bn_n_dot[4][0]
            yawdot = eta_bn_n_dot[5][0]
            wxdot = nu_bn_b_dot[3][0]
            wydot = nu_bn_b_dot[4][0]
            wzdot = nu_bn_b_dot[5][0]

            # Update state using Euler integration (no cumulative changes)
            x += xdot * integration_step
            y += ydot * integration_step
            z += zdot * integration_step
            vx += vxdot * integration_step
            vy += vydot * integration_step
            vz += vzdot * integration_step
            roll += rolldot * integration_step
            pitch += pitchdot * integration_step
            yaw += yawdot * integration_step
            wx += wxdot * integration_step
            wy += wydot * integration_step
            wz += wzdot * integration_step

            nu_bn_b = np.array([vx, vy, vz, wx, wy, wz]).reshape((6,1))

            # Update restoration torque after each step
            fg_B = R_b__n_inv(roll, pitch, yaw) @ fg_n
            g_CB = -np.block([[np.zeros((3, 1))],
                            [np.reshape(np.cross(r_gb__b, fg_B), (3, 1))]])

        # Final state values a68.91613303fter integration
        eta_bn_n = np.array([x, y, z, roll, pitch, yaw]).reshape((6,1))
        nu_bn_b = np.array([vx, vy, vz, wx, wy, wz]).reshape((6,1))

        nonlin_pred = np.concatenate((nu_bn_b, eta_bn_n), axis=0)
        
        return nonlin_pred


    
    def get_jax_pred(self, sim):
        print(f"Using Jax for prediction and inverse jac")
        curr_x = sim.get_var('x')
        curr_y = sim.get_var('y')
        curr_z = sim.get_var('z')
        curr_vx = sim.get_var('vx')
        curr_vy = sim.get_var('vy')
        curr_vz = sim.get_var('vz')
        curr_roll = sim.get_var('phi')
        curr_pitch = sim.get_var('theta')
        curr_yaw = sim.get_var('psi')
        curr_wx = sim.get_var('wx')
        curr_wy = sim.get_var('wy')
        curr_wz = sim.get_var('wz')

        STATE = jnp.array([curr_x, curr_y, curr_z, curr_vx, curr_vy, curr_vz, curr_roll, curr_pitch, curr_yaw, curr_wx, curr_wy, curr_wz])
        # u = self.last_input
        INPUT = jnp.array(self.last_input)
        # print(f"input.shape: \n{INPUT.shape}")

        
        integration_step = 0.01    
        # outputs = predict_outputs(STATE, INPUT, self.T_lookahead, integration_step, self.Cjax)
        outputs = rk4_pred(STATE, INPUT, self.T_lookahead, integration_step, self.Cjax)
        # print(f"{outputs = }")

        # adjusted_invjac, cond_number = compute_adjusted_invjac(STATE, INPUT, self.T_lookahead, integration_step, self.Cjax)
        adjusted_invjac, cond_number = rk4_invjac(STATE, INPUT, self.T_lookahead, integration_step, self.Cjax)
        print(f"cond_number: \n{cond_number}")


        outputs = np.array(outputs).reshape(-1, 1)
        self.jac_inv = np.array(adjusted_invjac)
        return outputs





    def get_prediction(self, sim):

        u = self.last_input
        pred = self.euler_integration(u, sim)
        # print(f"{pred = }")
        outputs = self.C @ pred

        epsilon = 1e-5

        u0_pert = epsilon * np.array([[1,0,0,0]]).T
        #print(f"{u0_pert= }")
        perturbed_u0 = u + u0_pert
        #print(f"{perturbed_u0 = }")
        pred = self.euler_integration(perturbed_u0, sim)
        var0_pred = self.C @ pred

        dpdu0 = (var0_pred - outputs)/epsilon

        u1_pert = epsilon * np.array([[0,1,0,0]]).T
        perturbed_u1 = u + u1_pert
        pred = self.euler_integration(perturbed_u1, sim)
        var1_pred = self.C @ pred
        dpdu1 = (var1_pred - outputs)/epsilon

        u2_pert = epsilon * np.array([[0,0,1,0]]).T
        perturbed_u2 = u + u2_pert
        pred = self.euler_integration(perturbed_u2, sim)
        var2_pred = self.C @ pred
        dpdu2 = (var2_pred - outputs)/epsilon

        u3_pert = epsilon * np.array([[0,0,0,1]]).T
        perturbed_u3 = u + u3_pert
        #print(f"{perturbed_u3 = }")

        pred = self.euler_integration(perturbed_u3, sim)
        var3_pred = self.C @ pred
        dpdu3 = (var3_pred - outputs)/epsilon

        #print(f"{outputs = }")
        #print(f"{var0_pred = }, \n{var1_pred = }, \n{var2_pred = }, \n{var3_pred = }")
        #print(f"{dpdu0 = }, \n{dpdu1 = }, \n{dpdu2 = }. \n{dpdu3 = }")
        jac_u = np.hstack([dpdu0, dpdu1, dpdu2, dpdu3]) 
        #print(f"{jac_u = }")
        inv_jac = np.linalg.inv(jac_u)

        self.jac_inv = inv_jac
        return np.array([[outputs[0][0], outputs[1][0], outputs[2][0], outputs[3][0]]]).T


    def update_cbf_history(self, cbf_data):
        self.cbf_history = np.append(self.cbf_history, cbf_data.reshape((1,4)), axis=0)


    def get_ctrl_action(self, sim):        
        print(f"------------------------------------------")
        print(f"Getting control action at time {sim.get_current_timestep()}")        
        sim.start_timer()
        n = sim.get_current_timestep()
        # print(f"{n = }")
        # if n > 3:
        #     sys.exit(1)
        
        if n >= len(self.traj_x)-5:
            return None

        t0 = time.time()
        # pred = self.get_prediction(sim)
        pred = self.get_jax_pred(sim)

        print(f"Pred: {pred}")
        # print(f"Pred2: {pred2}")
        # print(f"{self.jac_inv = }")
        # print(f"{self.jac_inv2 = }")

        # pred = pred2
        # self.jac_inv = self.jac_inv2

        pred[3][0] = self.normalize_angle(pred[3][0])
        error = self.get_tracking_error(sim, n, pred)
        NR = self.jac_inv @ error # calculates newton-raphson control input without speed-up parameter
        phi = NR # placeholder for if we apply Integral CBFs to the system

        #-------------------------------------
        # CBFs
        # Get current thrust (force) and rates
        last_input = self.last_input
        curr_fx = last_input[0][0]
        curr_fy = last_input[1][0]
        curr_fz = last_input[2][0]
        curr_tz = last_input[3][0]

        # Get current newton-raphson udot value we just calculated that we want to direct towards safe region(NR = (dg/du)^-1 * (yref - ypred)) (before alpha tuning)
        phi = NR
        phi_fx = phi[0][0]
        phi_fy = phi[1][0]
        phi_fz = phi[2][0]
        phi_tz = phi[3][0]

        max_fx = 0.035
        max_fy = 0.035
        max_fz = 0.4
        max_tz = 0.001


# SET UP CBF Fx
        v_fx = 0.0 # influence value initialized to 0 as default for if no CBF is needed
        gamma = 1.0 # CBF parameter
        thrust_max = max_fx # max thrust (force) value to limit thrust to
        thrust_min = -max_fx # min thrust (force) value to limit thrust to

        # print(f"curr_fz: {curr_fz}")
        # Optimization procedure for CBF
        if curr_fx >= 0:
            zeta = gamma * (thrust_max - curr_fx) - phi_fx
            if zeta < 0:
                v_fx = zeta

        if curr_fx < 0:
            zeta = -gamma * (-thrust_min + curr_fx) - phi_fx
            if zeta > 0:
                v_fx = zeta           

# SET UP CBF Fy
        v_fy = 0.0 # influence value initialized to 0 as default for if no CBF is needed
        gamma = 1.0 # CBF parameter
        thrust_max = max_fy # max thrust (force) value to limit thrust to
        thrust_min = -max_fy # min thrust (force) value to limit thrust to

        # print(f"curr_fz: {curr_fz}")
        # Optimization procedure for CBF
        if curr_fy >= 0:
            zeta = gamma * (thrust_max - curr_fy) - phi_fy
            if zeta < 0:
                v_fy = zeta

        if curr_fy < 0:
            zeta = -gamma * (-thrust_min + curr_fy) - phi_fy
            if zeta > 0:
                v_fy = zeta

# CBF FOR Fz
        v_fz = 0.0 # influence value initialized to 0 as default for if no CBF is needed
        gamma = 1.0 # CBF parameter
        thrust_max = max_fz # max thrust (force) value to limit thrust to
        thrust_min = -max_fz # min thrust (force) value to limit thrust to

        # print(f"curr_fz: {curr_fz}")
        # Optimization procedure for CBF
        if curr_fz >= 0:
            zeta = gamma * (thrust_max - curr_fz) - phi_fz
            if zeta < 0:
                v_fz = zeta

        if curr_fz < 0:
            zeta = -gamma * (-thrust_min + curr_fz) - phi_fz
            if zeta > 0:
                v_fz = zeta
    

# SET UP CBF Tz
        v_tz = 0.0 # influence value initialized to 0 as default for if no CBF is needed
        gamma = 1.0 # CBF parameter
        rates_max = max_tz 
        rates_min = -max_tz
        # Optimization procedure for CBF
        if curr_tz >= 0:
            zeta = gamma * (rates_max - curr_tz) - phi_tz
            if zeta < 0:
                v_tz = zeta
        elif curr_tz < 0:
            zeta = -gamma * (-rates_min + curr_tz) - phi_tz
            if zeta > 0:
                v_tz = zeta


        if self.use_CBFs:
            v = np.array([[v_fx, v_fy, v_fz, v_tz]]).T
        else:
            v = np.array([[0., 0., 0. ,0.]]).T # placeholder for if we apply Integral CBFs to the system 
        # print(f"{'Using CBFs' if self.use_CBFs else 'Not using CBFs:'}\nv: {v}")
        self.update_cbf_history(v)
        
        udot = phi + v # placeholder for if we apply Integral CBFs to the system
        change_u = udot * self.dT
        u = self.last_input + self.alpha * change_u

        print(f"Total NR Comp Time: {time.time() - t0 = }")
        print(f"{pred = }")
        print(f"{error = }")
        print(f"{NR = }")
        print(f"{udot = }")
        print(f"{change_u = }")
        print(f"prev_u: {self.last_input}")
        print(f"{u = }")
        print(f"------------------------------------------\n")
        if np.isnan(u).any():
            print("NAN in control input")
            sys.exit(1)

        sim.end_timer()

        self.last_input = u
        return u.reshape((4,1))
