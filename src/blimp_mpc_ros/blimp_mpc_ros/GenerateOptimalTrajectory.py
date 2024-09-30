# Generate an optimal trajectory that flies a blimp from a start point to an end point
# while minimizing the two-norm of the input.
# Assume that the blimp starts at rest.
# Save the result to a file that can be loaded by Trajectories.py.

import numpy as np
import matplotlib.pyplot as plt
import casadi as ca
from BlimpSim import BlimpSim

# Fly the blimp from its current location to a point (2,2), in 15 seconds.
# The blimp starts at rest.

# Time
final_time = 15
dT = 0.05
n = int(final_time / dT)

# Initialize
x_0 = np.zeros(12)
x_f = np.zeros(12)
x_f[6] = 2
x_f[7] = 2

opti = ca.Opti()
opti_x = opti.variable(12, n)
opti_u = opti.variable(4, n)

max_fx = 0.035
max_fy = 0.035
max_fz = 0.2 # TODO: increase this to 0.908?
max_tz = 0.001

R = np.array([
    [1/(max_fx**2), 0, 0, 0],
    [0, 1/(max_fy**2), 0, 0],
    [0, 0, 1/(max_fz**2), 0],
    [0, 0, 0, 1/(max_tz**2)]
])

opts_setting = {
    'ipopt.max_iter': 2000
}

opti.solver('ipopt', opts_setting)

# Initial condition.
opti.subject_to( opti_x[:,0] == x_0 )

# Create the dynamics equality constraints
for j in range(n-1):
    x_next = opti_x[:,j] + dT * BlimpSim.f(opti_x[:,j], opti_u[:,j])
    opti.subject_to( opti_x[:,j+1] == x_next )

# Target
opti.subject_to( opti_x[:,n-1] == x_f )

# Create the cost function.
obj = 0
gamma = 1 # Weighting on the control effort.
for i in range(n):
    # Penalize the control effort.
    obj += gamma * ca.mtimes([opti_u[:,i].T, R, opti_u[:,i]])

# Bound the control input variables.
opti.subject_to( opti.bounded(-max_fx, opti_u[0,:], max_fx) )
opti.subject_to( opti.bounded(-max_fy, opti_u[1,:], max_fy) )
opti.subject_to( opti.bounded(-max_fz, opti_u[2,:], max_fz) )
opti.subject_to( opti.bounded(-max_tz, opti_u[3,:], max_tz) )

opti.minimize(obj)

solution = opti.solve()

u = solution.value(opti_u)
x = solution.value(opti_x)
print(x)
print(x.shape)

# Plot the results.
plt.figure()
plt.plot(x[6,:], x[7,:])
plt.title('Optimal trajectory')
plt.xlabel('x')
plt.ylabel('y')

# Plot x and y velocities.
plt.figure()
plt.plot(x[0,:], label='x vel')
plt.plot(x[1,:], label='y vel')
plt.title('Velocity')
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.legend()

plt.show()

# Save the trajectory (u and x)
np.save('optimal_trajectory', {'u': u, 'x': x})
