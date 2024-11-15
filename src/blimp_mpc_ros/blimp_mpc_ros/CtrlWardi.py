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
        self.enhanced_predictor = True
        self.alpha = np.array([[30, 30, 30, 20]]).T
        self.T_lookahead = 1.2
        self.dT = dT

        MASS = 0.15
        GRAVITY = 9.806
        self.last_input = np.array([[0.0, 0.0, -1*MASS*GRAVITY, 0.0]]).T

        self.metadata = np.array([
            str(self.alpha),
        ])

        C = np.zeros([4,12])
        C[0,6],C[1,7], C[2,8], C[3,11] = 1,1,1,1
        self.C = C

        C = np.zeros([4,12])
        C[0,0],C[1,1], C[2,2], C[3,8] = 1,1,1,1
        self.Cjax = C

        self.cbf_history =  np.zeros((1,4))

    def uncompiled_euler_integration(self, u, sim): 
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

    def uncompiled_prediction(self, sim):

        u = self.last_input
        pred = self.uncompiled_euler_integration(u, sim)
        # print(f"{pred = }")
        outputs = self.C @ pred

        epsilon = 1e-5

        u0_pert = epsilon * np.array([[1,0,0,0]]).T
        #print(f"{u0_pert= }")
        perturbed_u0 = u + u0_pert
        #print(f"{perturbed_u0 = }")
        pred = self.uncompiled_euler_integration(perturbed_u0, sim)
        var0_pred = self.C @ pred

        dpdu0 = (var0_pred - outputs)/epsilon

        u1_pert = epsilon * np.array([[0,1,0,0]]).T
        perturbed_u1 = u + u1_pert
        pred = self.uncompiled_euler_integration(perturbed_u1, sim)
        var1_pred = self.C @ pred
        dpdu1 = (var1_pred - outputs)/epsilon

        u2_pert = epsilon * np.array([[0,0,1,0]]).T
        perturbed_u2 = u + u2_pert
        pred = self.uncompiled_euler_integration(perturbed_u2, sim)
        var2_pred = self.C @ pred
        dpdu2 = (var2_pred - outputs)/epsilon

        u3_pert = epsilon * np.array([[0,0,0,1]]).T
        perturbed_u3 = u + u3_pert
        #print(f"{perturbed_u3 = }")

        pred = self.uncompiled_euler_integration(perturbed_u3, sim)
        var3_pred = self.C @ pred
        dpdu3 = (var3_pred - outputs)/epsilon

        #print(f"{outputs = }")
        #print(f"{var0_pred = }, \n{var1_pred = }, \n{var2_pred = }, \n{var3_pred = }")
        #print(f"{dpdu0 = }, \n{dpdu1 = }, \n{dpdu2 = }. \n{dpdu3 = }")
        jac_u = np.hstack([dpdu0, dpdu1, dpdu2, dpdu3]) 
        #print(f"{jac_u = }")
        inv_jac = np.linalg.inv(jac_u)

        self.jac_invU = inv_jac
        return np.array([[outputs[0][0], outputs[1][0], outputs[2][0], outputs[3][0]]]).T

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
        INPUT = jnp.array(self.last_input)

        
        integration_step = 0.01  
        predictor_type = 'rk4' # 'euler or 'rk4'
        outputs, invjacU, cond_number, enhance_term = output_predictor(STATE, INPUT, self.T_lookahead, integration_step, self.Cjax, predictor_type, self.enhanced_predictor) 
        print(f"{outputs = }")
        print(f"{invjacU = }")
        print(f"cond_number: \n{cond_number}")
        print(f"enhance_term: \n{enhance_term}")

        outputs = np.array(outputs).reshape(-1, 1)
        enhance_term = np.array(enhance_term).reshape(-1, 1)
        self.jac_invU = np.array(invjacU)
        return outputs, enhance_term

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
        n_lookahead = int(self.T_lookahead / self.dT)
        n_plus_lookahead = n + n_lookahead
        print(f"CURR: {[sim.get_var('x'), sim.get_var('y'), sim.get_var('z'), sim.get_var('psi')]}")
        print(f"REF: {[self.traj_x[n_plus_lookahead], self.traj_y[n_plus_lookahead], self.traj_z[n_plus_lookahead], self.traj_psi[n_plus_lookahead]]}")

        err_x = self.traj_x[n_plus_lookahead] - pred[0][0] 
        err_y = self.traj_y[n_plus_lookahead] - pred[1][0]
        err_z = self.traj_z[n_plus_lookahead] - pred[2][0]
        err_psi = self.shortest_path_yaw(self.traj_psi[n_plus_lookahead], pred[3][0])
        print(f"ERR: {[err_x, err_y, err_z, err_psi]}")
        return np.array([[err_x, err_y, err_z, err_psi]]).T
    
    def enhance(self, sim, n, pred, enhance_term):
        n_lookahead = int(self.T_lookahead / self.dT)
        n_plus_lookahead = n + n_lookahead
        print(f"CURR: {[sim.get_var('x'), sim.get_var('y'), sim.get_var('z'), sim.get_var('psi')]}")
        print(f"REF: {[self.traj_x_dot[n_plus_lookahead], self.traj_y_dot[n_plus_lookahead], self.traj_z_dot[n_plus_lookahead], self.traj_psi_dot[n_plus_lookahead]]}")
        err_xd = self.traj_x_dot[n_plus_lookahead] - enhance_term[0][0]
        err_yd = self.traj_y_dot[n_plus_lookahead] - enhance_term[1][0]
        err_zd = self.traj_z_dot[n_plus_lookahead] - enhance_term[2][0]
        err_psid = self.traj_psi_dot[n_plus_lookahead] - enhance_term[3][0]

        # print(f"ERRD: {[err_xd, err_yd, err_zd, err_psid]}")
        return np.array([[err_xd, err_yd, err_zd, err_psid]]).T

    def apply_CBFs(self, phi):
        v = np.array([[0., 0., 0. ,0.]]).T # placeholder for if we don't want to apply Integral CBFs to the system 
        if self.use_CBFs:
            print(f"{self.use_CBFs = }")
            # Get current thrust (force) and rates
            curr_fx = self.last_input[0][0]
            curr_fy = self.last_input[1][0]
            curr_fz = self.last_input[2][0]
            curr_tz = self.last_input[3][0]

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

            
            v = np.array([[v_fx, v_fy, v_fz, v_tz]]).T

        # print(f"{'Using CBFs' if self.use_CBFs else 'Not using CBFs:'}\nv: {v}")
        self.update_cbf_history(v)
        return v
    
    def get_ctrl_action(self, sim):        
        print(f"------------------------------------------")
        print(f"Getting control action at time {sim.get_current_timestep()}")        
        sim.start_timer()
        n = sim.get_current_timestep()
        if n >= len(self.traj_x)-5:
            return None

        t0 = time.time()
        pred, enhance_term = self.get_jax_pred(sim) #self.uncompiled_prediction(sim)
        base_error = self.get_tracking_error(sim, n, pred)
        enhanced_error = self.enhance(sim, n, pred, enhance_term) if self.enhanced_predictor else np.zeros((4,1))
        total_err = self.alpha * base_error + enhanced_error
        NR = self.jac_invU @ total_err
        v = self.apply_CBFs(NR)
        udot = NR + v
        change_u = udot * self.dT
        u = self.last_input + change_u
        t1 = time.time()

        print(f"\nTotal NR Comp Time: {t1 - t0 = }")
        print(f"{self.use_CBFs = }")
        print(f"{self.enhanced_predictor = }")
        print(f"{base_error = }")
        print(f"{enhanced_error = }")
        print(f"{total_err = }")
        print(f"{NR = }")
        print(f"{v = }")
        print(f"{udot = }")
        print(f"{change_u = }")
        print(f"prev_u: {self.last_input}")
        print(f"{u = }\n")
        print(f"------------------------------------------\n")
        if np.isnan(u).any():
            print("NAN in control input")
            sys.exit(1)

        sim.end_timer()
        self.last_input = u
        return u.reshape((4,1))

    def update_cbf_history(self, cbf_data):
        self.cbf_history = np.append(self.cbf_history, cbf_data.reshape((1,4)), axis=0)
