import jax
import jax.numpy as jnp
from jax import jit, jacfwd, lax


# ~~ The following functions have the various non-linear models and neural networks for predicting the system output state ~~
    def get_jax_predict(self, last_input): #Predicts System Output State Using Jax
        """ Predicts the system output state using a numerically integrated nonlinear model. """
        if self.nonlin0: 
            print(f"0 order hold jax")
            # t1 = time.time()
            STATE = jnp.array([self.state_vector[0][0], self.state_vector[1][0], self.state_vector[2][0], self.state_vector[3][0], self.state_vector[4][0], self.state_vector[5][0], self.state_vector[6][0], self.state_vector[7][0], self.state_vector[8][0]])
            INPUT = jnp.array([-last_input[0][0], last_input[1][0], last_input[2][0], last_input[3][0]])
            # print(f"STATE: \n{STATE}")
            outputs = predict_outputs(STATE, INPUT, self.T_LOOKAHEAD, self.GRAVITY, self.MASS, self.C, integration_step=0.1)
            # print(f"Outputs: \n{outputs}")
            adjusted_invjac = compute_adjusted_invjac(STATE, INPUT, self.T_LOOKAHEAD, self.GRAVITY, self.MASS, self.C, integration_step=0.1)
            # print(f"adjusted_invjac: \n{adjusted_invjac}")


            outputs = np.array(outputs).reshape(-1, 1)
            # print(f"{outputs = }")
            # print(f"{type(outputs) = }")
            adjusted_invjac = np.array(adjusted_invjac)
            # print(f"{adjusted_invjac = }")
            # print(f"{type(adjusted_invjac) = }")
            self.jac_inv = adjusted_invjac

            # exit(0)
            return outputs
        
############################### 0 Order Hold Functions ###############################
@jit
def dynamics(state, inputs, g, m):
    x, y, z, vx, vy, vz, roll, pitch, yaw = state
    curr_thrust, curr_rolldot, curr_pitchdot, curr_yawdot = inputs

    sr = jnp.sin(roll)
    sy = jnp.sin(yaw)
    sp = jnp.sin(pitch)
    cr = jnp.cos(roll)
    cp = jnp.cos(pitch)
    cy = jnp.cos(yaw)

    vxdot = -(curr_thrust / m) * (sr * sy + cr * cy * sp)
    vydot = -(curr_thrust / m) * (cr * sy * sp - cy * sr)
    vzdot = g - (curr_thrust / m) * (cr * cp)

    return jnp.array([vx, vy, vz, vxdot, vydot, vzdot, curr_rolldot, curr_pitchdot, curr_yawdot])

# Function to integrate dynamics over time
@jit
def integrate_dynamics(state, inputs, integration_step, integrations_int, g, m):
    def for_function(i, current_state):
        return current_state + dynamics(current_state, inputs, g, m) * integration_step

    pred_state = lax.fori_loop(0, integrations_int, for_function, state)
    return pred_state

# Prediction function
@jit
def predict_states(state, last_input, T_lookahead, g, m, integration_step=0.1):
    inputs = last_input.flatten()
    integrations_int = 8 #int(T_lookahead / integration_step)
    pred_state = integrate_dynamics(state, inputs, integration_step, integrations_int, g, m)
    return pred_state

# Prediction function
@jit
def predict_outputs(state, last_input, T_lookahead, g, m, C, integration_step=0.1):
    inputs = last_input.flatten()
    integrations_int = 8 #int(T_lookahead / integration_step)
    pred_state = integrate_dynamics(state, inputs, integration_step, integrations_int, g, m)
    return C@pred_state

# Compute Jacobian
@jit
def compute_jacobian(state, last_input, T_lookahead, g, m, C, integration_step):
    jac_fn = jacfwd(lambda x: predict_outputs(state, x, T_lookahead, g, m, C, integration_step))
    return jac_fn(last_input)

# Compute adjusted inverse Jacobian
@jit
def compute_adjusted_invjac(state, last_input, T_lookahead, g, m, C, integration_step):
    jac = compute_jacobian(state, last_input, T_lookahead, g, m, C, integration_step)
    inv_jacobian = jnp.linalg.pinv(jac)
    inv_jacobian_modified = inv_jacobian.at[:, 2].set(-inv_jacobian[:, 2])
    return inv_jacobian_modified
