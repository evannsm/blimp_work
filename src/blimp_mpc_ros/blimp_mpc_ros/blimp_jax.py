import jax
import jax.numpy as jnp
from jax import jit, jacfwd, lax


## Cross product operator (S operator)
@jit
def S(r):
    return jnp.block([[  0,       -r[2],    r[1]],
                     [r[2],     0,      -r[0]],
                     [-r[1],    r[0],      0]])

@jit
def H(r):
    return jnp.block([[jnp.identity(3), S(r).T],
                     [jnp.zeros((3, 3)), jnp.identity(3)]])

## Rotation matrices
@jit
def R_b__n(phi, theta, psi):
    x_rot = jnp.array([[1,         0,           0],
                      [0,       jnp.cos(phi),   - jnp.sin(phi)],
                      [0,       jnp.sin(phi),    jnp.cos(phi)]])
    y_rot = jnp.array([[ jnp.cos(theta),      0,        jnp.sin(theta)],
                      [0,         1,           0],
                      [- jnp.sin(theta),     0,        jnp.cos(theta)]])
    z_rot = jnp.array([[ jnp.cos(psi),    - jnp.sin(psi),       0],
                      [ jnp.sin(psi),     jnp.cos(psi),       0],
                      [0,          0,           1]])
    return z_rot @ y_rot @ x_rot

@jit
def R_b__n_inv(phi, theta, psi):
    return jnp.array([[ jnp.cos(psi)* jnp.cos(theta), jnp.cos(theta)* jnp.sin(psi), - jnp.sin(theta)],
                     [ jnp.cos(psi)* jnp.sin(phi)* jnp.sin(theta) - jnp.cos(phi)* jnp.sin(psi), 
                      jnp.cos(phi)* jnp.cos(psi) + jnp.sin(phi)* jnp.sin(psi)* jnp.sin(theta), 
                      jnp.cos(theta)* jnp.sin(phi)],
                     [ jnp.sin(phi)* jnp.sin(psi) + jnp.cos(phi)* jnp.cos(psi)* jnp.sin(theta), 
                      jnp.cos(phi)* jnp.sin(psi)* jnp.sin(theta) - jnp.cos(psi)* jnp.sin(phi), 
                      jnp.cos(phi)* jnp.cos(theta)]])

## Transformation matrix for angular velocity
@jit
def T(phi, theta):
    return jnp.array([[1,     jnp.sin(phi)* jnp.tan(theta),      jnp.cos(phi)* jnp.tan(theta)],
                     [0,          jnp.cos(phi),                   - jnp.sin(phi)],
                     [0,     jnp.sin(phi)/jnp.cos(theta),      jnp.cos(phi)/jnp.cos(theta)]])


Henv = 0.51  # Height of the envelope (m)
Hgon = 0.04  # Height of the gondola (m)
r_z_gb__b = 0.05  # Distance from CG to CB (m)
dvt = Henv / 2 + Hgon # Distance from CB to motor thrust application point
r_z_tg__b = dvt - r_z_gb__b  # Distance from CB to thrust generation point
r_z_gb__b = 0.05
r_gb__b = jnp.array([0, 0, r_z_gb__b]).T

# Mass and inertia properties
m_RB = 0.1249  # Mass of the blimp (kg)
I_RBx = 0.005821  # Rotational inertia about x-axis (kg.m^2)
M_RB_CG = jnp.diag(jnp.array([m_RB, m_RB, m_RB, I_RBx, I_RBx, I_RBx]))# Inertia matrix for the rigid body in body frame


M_RB_CB = H(r_gb__b).T @ M_RB_CG @ H(r_gb__b)
M_A_CB = jnp.diag(jnp.array([0.0466, 0.0466, 0.0545, 0.0, 0.0, 0.0])) # Added mass and inertia matrix (assuming hydrodynamics)

# Total inertia matrix at the center of buoyancy
M_CB = M_RB_CB + M_A_CB
M_CB_inv = jnp.linalg.inv(M_CB)

# Gravitational force in the navigation frame
g_acc = 9.8  # Gravitational acceleration (m/s^2)
fg_n = m_RB * jnp.array([0, 0, g_acc]).T  # Force due to gravity

# Aerodynamic damping matrix
D_CB = jnp.diag(jnp.array([0.0125, 0.0125, 0.0480, 0.000862, 0.000862, 0.000862]))



## Coriolis matrix
@jit
def C(M, nu):
    dimM = jnp.shape(M)[0]
    M11 = M[0:int(dimM/2), 0:int(dimM/2)]
    M12 = M[0:int(dimM/2), int(dimM/2):dimM]
    M21 = M[int(dimM/2):dimM, 0:int(dimM/2)]
    M22 = M[int(dimM/2):dimM, int(dimM/2):dimM]
    dimNu = jnp.shape(nu)[0]
    nu1 = nu[0:int(dimNu/2)]
    nu2 = nu[int(dimNu/2):dimNu]
    return jnp.block([[ jnp.zeros((3, 3)),    -S(M11 @ nu1 + M12 @ nu2)],
                     [-S(M11 @ nu1 + M12 @ nu2), -S(M21 @ nu1 + M22 @ nu2)]])

@jit
def dynamics(state, u):
        curr_x, curr_y, curr_z, curr_vx, curr_vy, curr_vz, curr_roll, curr_pitch, curr_yaw, curr_wx, curr_wy, curr_wz = state
        tau_B = jnp.array([u[0][0],
                        u[1][0],
                        u[2][0],
                        -r_z_tg__b * u[1][0],
                        r_z_tg__b * u[0][0],
                        u[3][0]]).reshape((6,1))
        
        nu_bn_b = jnp.array([curr_vx, curr_vy, curr_vz, curr_wx, curr_wy, curr_wz]).reshape((6,1))
        fg_B = R_b__n_inv(curr_roll, curr_pitch, curr_yaw) @ fg_n
        g_CB = -jnp.block([[jnp.zeros((3, 1))],
                        [jnp.reshape(jnp.cross(r_gb__b, fg_B), (3, 1))]])
        
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


        # Update state derivatives
        eta_bn_n_dot = jnp.block([[R_b__n(roll, pitch, yaw), jnp.zeros((3, 3))],
                                [jnp.zeros((3, 3)), T(roll, pitch)]]) @ nu_bn_b

        nu_bn_b_dot = jnp.reshape(-M_CB_inv @ (C(M_CB, nu_bn_b) @ nu_bn_b + 
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


        return jnp.array([xdot, ydot, zdot, vxdot, vydot, vzdot, rolldot, pitchdot, yawdot, wxdot, wydot, wzdot])



# Function to integrate dynamics over time
@jit
def integrate_dynamics(state, inputs, integration_step, integrations_int):
    def for_function(i, current_state):
        return current_state + dynamics(current_state, inputs) * integration_step

    pred_state = lax.fori_loop(0, integrations_int, for_function, state)
    return pred_state

# Prediction function
@jit
def predict_outputs(state, last_input, T_lookahead, C, integration_step, integrations_int):
    inputs = last_input
    pred_state = integrate_dynamics(state, inputs, integration_step, integrations_int)
    # print(f"{pred_state = }")
    return C@pred_state


# Compute Jacobian
@jit
def compute_jacobian(state, last_input, T_lookahead, C, integration_step, integrations_int):
    jac_fn = jacfwd(lambda x: predict_outputs(state, x, T_lookahead, C, integration_step, integrations_int))
    return jac_fn(last_input).reshape(4,4)

# Compute adjusted inverse Jacobian
@jit
def compute_adjusted_invjac(state, last_input, T_lookahead, C, integration_step, integrations_int):
    jac = compute_jacobian(state, last_input, T_lookahead, C, integration_step, integrations_int)

    regularization_term = 1e-9
    jac += jnp.eye(jac.shape[0]) * regularization_term
    
    cond_number = jnp.linalg.cond(jac)
    inv_jacobian = jnp.linalg.pinv(jac)

    return inv_jacobian, cond_number