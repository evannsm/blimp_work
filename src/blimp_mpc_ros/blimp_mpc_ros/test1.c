#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Define a struct for the output vector
typedef struct {
    double x, y, z, vx, vy, vz, roll, pitch, yaw;
} Vector9x1;

// Cross product operator (S operator)
void cross_product_operator(double r[3], double S[3][3]) {
    S[0][0] = 0.0;        S[0][1] = -r[2];  S[0][2] = r[1];
    S[1][0] = r[2];       S[1][1] = 0.0;    S[1][2] = -r[0];
    S[2][0] = -r[1];      S[2][1] = r[0];   S[2][2] = 0.0;
}

// Rotation matrix R_b__n (from body to navigation frame)
void rotation_matrix(double phi, double theta, double psi, double R_b__n[3][3]) {
    double x_rot[3][3] = {{1.0, 0.0, 0.0},
                          {0.0, cos(phi), -sin(phi)},
                          {0.0, sin(phi), cos(phi)}};

    double y_rot[3][3] = {{cos(theta), 0.0, sin(theta)},
                          {0.0, 1.0, 0.0},
                          {-sin(theta), 0.0, cos(theta)}};

    double z_rot[3][3] = {{cos(psi), -sin(psi), 0.0},
                          {sin(psi), cos(psi), 0.0},
                          {0.0, 0.0, 1.0}};

    // Multiply matrices: R_b__n = z_rot @ y_rot @ x_rot
    double temp[3][3];
    multiply_matrices(z_rot, y_rot, temp);
    multiply_matrices(temp, x_rot, R_b__n);
}

// Matrix multiplication function
void multiply_matrices(double a[3][3], double b[3][3], double result[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            result[i][j] = 0.0;
            for (int k = 0; k < 3; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

// Coriolis matrix calculation
void coriolis_matrix(double M[6][6], double nu[6], double C[6][6]) {
    double S_nu1[3][3], S_nu2[3][3];
    double nu1[3] = {nu[0], nu[1], nu[2]};
    double nu2[3] = {nu[3], nu[4], nu[5]};

    double M11[3][3] = {{M[0][0], M[0][1], M[0][2]}, {M[1][0], M[1][1], M[1][2]}, {M[2][0], M[2][1], M[2][2]}};
    double M12[3][3] = {{M[0][3], M[0][4], M[0][5]}, {M[1][3], M[1][4], M[1][5]}, {M[2][3], M[2][4], M[2][5]}};
    double M21[3][3] = {{M[3][0], M[3][1], M[3][2]}, {M[4][0], M[4][1], M[4][2]}, {M[5][0], M[5][1], M[5][2]}};
    double M22[3][3] = {{M[3][3], M[3][4], M[3][5]}, {M[4][3], M[4][4], M[4][5]}, {M[5][3], M[5][4], M[5][5]}};

    cross_product_operator(nu1, S_nu1);
    cross_product_operator(nu2, S_nu2);

    // Block matrix for Coriolis matrix
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            C[i][j] = 0.0;  // Zero matrix in upper-left block
            C[i][j + 3] = -M11[i][0] * nu1[0] - M12[i][0] * nu2[0];
            C[i + 3][j] = -M21[i][0] * nu1[0] - M22[i][0] * nu2[0];
            C[i + 3][j + 3] = -S_nu2[i][0];
        }
    }
}

// Main function to perform calculations
Vector9x1* performCalculations(double g_acc, double m_RB, double I_RBx, double dvt, double curr_x, double curr_y, double curr_z,
                               double curr_vx, double curr_vy, double curr_vz, double curr_roll, double curr_pitch, double curr_yaw,
                               double curr_wx, double curr_wy, double curr_wz, double u[4], double integration_step, int integrations_int) {

    double r_gb__b[3] = {0.0, 0.0, 0.05};
    double M_RB_CB[6][6] = {{m_RB, 0, 0, 0, 0, 0},
                            {0, m_RB, 0, 0, 0, 0},
                            {0, 0, m_RB, 0, 0, 0},
                            {0, 0, 0, I_RBx, 0, 0},
                            {0, 0, 0, 0, I_RBx, 0},
                            {0, 0, 0, 0, 0, I_RBx}};

    double tau_B[6] = {u[0], u[1], u[2], -dvt * u[1], dvt * u[0], u[3]};
    double nu_bn_b[6] = {curr_vx, curr_vy, curr_vz, curr_wx, curr_wy, curr_wz};

    double fg_n[3] = {0.0, 0.0, m_RB * g_acc}; // Gravitational force
    double fg_B[3];
    double g_CB[6] = {0.0}; // Initialize g_CB with zeros

    // Rotation matrices
    double R_b__n_inv[3][3];
    rotation_matrix(curr_roll, curr_pitch, curr_yaw, R_b__n_inv);

    // Cross product and gravity terms
    fg_B[0] = R_b__n_inv[0][0] * fg_n[0] + R_b__n_inv[0][1] * fg_n[1] + R_b__n_inv[0][2] * fg_n[2];
    fg_B[1] = R_b__n_inv[1][0] * fg_n[0] + R_b__n_inv[1][1] * fg_n[1] + R_b__n_inv[1][2] * fg_n[2];
    fg_B[2] = R_b__n_inv[2][0] * fg_n[0] + R_b__n_inv[2][1] * fg_n[1] + R_b__n_inv[2][2] * fg_n[2];

    double cross[3][3];
    cross_product_operator(r_gb__b, cross);
    g_CB[3] = cross[0][0] * fg_B[0] + cross[0][1] * fg_B[1] + cross[0][2] * fg_B[2];
    g_CB[4] = cross[1][0] * fg_B[0] + cross[1][1] * fg_B[1] + cross[1][2] * fg_B[2];
    g_CB[5] = cross[2][0] * fg_B[0] + cross[2][1] * fg_B[1] + cross[2][2] * fg_B[2];

    // Integrate over time
    for (int i = 0; i < integrations_int; i++) {
        // Calculate Coriolis matrix
        double C[6][6];
        coriolis_matrix(M_RB_CB, nu_bn_b, C);

        // Compute state derivatives and update
        for (int j = 0; j < 6; j++) {
            double nu_bn_b_dot = -(M_RB_CB[j][j] + C[j][j]) * nu_bn_b[j] - g_CB[j] + tau_B[j];
            nu_bn_b[j] += nu_bn_b_dot * integration_step;
        }

        curr_x += nu_bn_b[0] * integration_step;
        curr_y += nu_bn_b[1] * integration_step;
        curr_z += nu_bn_b[2] * integration_step;
        curr_roll += nu_bn_b[3] * integration_step;
        curr_pitch += nu_bn_b[4] * integration_step;
        curr_yaw += nu_bn_b[5] * integration_step;
    }

    // Allocate memory for the output vector
    Vector9x1* result = (Vector9x1*)malloc(sizeof(Vector9x1));

    // Populate the output vector
    result->x = curr_x;
    result->y = curr_y;
    result->z = curr_z;
    result->vx = nu_bn_b[0];
    result->vy = nu_bn_b[1];
    result->vz = nu_bn_b[2];
    result->roll = curr_roll;
    result->pitch = curr_pitch;
    result->yaw = curr_yaw;

    return result; // Return a pointer to the output vector
}

int main() {
    // Example usage
    double g_acc = 9.81;
    double m_RB = 0.1249;
    double I_RBx = 0.005821;
    double dvt = 0.235;  // Distance from CB to thrust generation point

    double u[4] = {1.0, 0.5, 0.2, 0.1};  // Thrust and torque inputs
    double curr_x = 0.0, curr_y = 0.0, curr_z = 0.0;
    double curr_vx = 0.1, curr_vy = 0.1, curr_vz = 0.1;
    double curr_roll = 0.1, curr_pitch = 0.1, curr_yaw = 0.1;
    double curr_wx = 0.01, curr_wy = 0.01, curr_wz = 0.01;

    double integration_step = 0.01;
    int integrations = 100;

    Vector9x1* result = performCalculations(g_acc, m_RB, I_RBx, dvt, curr_x, curr_y, curr_z, 
                                            curr_vx, curr_vy, curr_vz, curr_roll, curr_pitch, 
                                            curr_yaw, curr_wx, curr_wy, curr_wz, u, 
                                            integration_step, integrations);

    // Print the result
    printf("Final state after integration:\n");
    printf("Position: (%f, %f, %f)\n", result->x, result->y, result->z);
    printf("Velocity: (%f, %f, %f)\n", result->vx, result->vy, result->vz);
    printf("Orientation: (Roll: %f, Pitch: %f, Yaw: %f)\n", result->roll, result->pitch, result->yaw);

    // Free the allocated memory
    free(result);

    return 0;
}
