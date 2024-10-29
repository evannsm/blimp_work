def S(r):
    return np.block([[  0,       -r[2],    r[1]],
                     [r[2],     0,      -r[0]],
                     [-r[1],    r[0],      0]])

def C(M, nu):
    dimM = np.shape(M)[0]

    M11 = M[0:int(dimM/2), 0:int(dimM/2)]
    M12 = M[0:int(dimM/2), int(dimM/2):dimM]
    M21 = M[int(dimM/2):dimM, 0:int(dimM/2)]
    M22 = M[int(dimM/2):dimM, int(dimM/2):dimM]

    dimNu = np.shape(nu)[0]
    nu1 = nu[0:int(dimNu/2)]
    nu2 = nu[int(dimNu/2):dimNu]

    return np.block([[ np.zeros((3, 3)),    -S(M11@nu1 + M12@nu2)],
                     [-S(M11@nu1 + M12@nu2), -S(M21@nu1 + M22@nu2)]])

def R_b__n(phi, theta, psi):

    x_rot = np.array([[1,         0,           0],
                      [0,       np.cos(phi),   -np.sin(phi)],
                      [0,       np.sin(phi),    np.cos(phi)]])

    y_rot = np.array([[np.cos(theta),      0,        np.sin(theta)],
                      [0,         1,           0],
                      [-np.sin(theta),     0,        np.cos(theta)]])
    
    z_rot = np.array([[np.cos(psi),    -np.sin(psi),       0],
                      [np.sin(psi),     np.cos(psi),       0],
                      [0,          0,           1]])

    # World-to-body
    return z_rot @ y_rot @ x_rot


def T(phi, theta):
    
    return np.array([[1,     np.sin(phi)*np.tan(theta),      np.cos(phi)*np.tan(theta)],
                     [0,          np.cos(phi),                   -np.sin(phi)],
                     [0,     np.sin(phi)/np.cos(theta),      np.cos(phi)/np.cos(theta)]])

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

        # Final state values after integration
        eta_bn_n = np.array([x, y, z, roll, pitch, yaw]).reshape((6,1))
        nu_bn_b = np.array([vx, vy, vz, wx, wy, wz]).reshape((6,1))

        nonlin_pred = np.concatenate((nu_bn_b, eta_bn_n), axis=0)
        
        return nonlin_pred