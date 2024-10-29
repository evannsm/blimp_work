#include <iostream>  // For input/output
#include <Eigen/Dense>  // For Eigen matrix and vector operations
#include <cmath>  // For trigonometric functions

// Blimp geometry parameters
const double Henv = 0.51;  // Height of the envelope (m)
const double Hgon = 0.04;  // Height of the gondola (m)
double r_z_gb__b = 0.05;  // Distance from CG to CB (m)

// Distance from CB to motor thrust application point
double dvt = Henv / 2 + Hgon;
double r_z_tg__b = dvt - r_z_gb__b;  // Distance from CB to thrust generation point

// Mass and inertia properties
const double m_RB = 0.1249;  // Mass of the blimp (kg)
const double I_RBx = 0.005821;  // Rotational inertia about x-axis (kg.m^2)

// Inertia matrix for the rigid body in body frame (Initialized globally)
Eigen::Matrix<double, 6, 6> M_RB_CG = Eigen::Matrix<double, 6, 6>::Zero();  // 6x6 matrix

// Skew-symmetric matrix function (S(r)) to form the cross product matrix
Eigen::Matrix3d S(const Eigen::Vector3d& r) {
    Eigen::Matrix3d S_r;
    S_r <<    0,  -r(2),  r(1),
           r(2),     0,  -r(0),
          -r(1),  r(0),     0;
    return S_r;
}

// Transformation matrix H(r)
Eigen::Matrix<double, 6, 6> H(const Eigen::Vector3d& r) {
    Eigen::Matrix<double, 6, 6> H_r;
    H_r << Eigen::Matrix3d::Identity(), S(r).transpose(),
           Eigen::Matrix3d::Zero(), Eigen::Matrix3d::Identity();
    return H_r;
}

// Rotation matrix from body frame to navigation frame (R_b__n)
Eigen::Matrix3d R_b__n(double phi, double theta, double psi) {
    Eigen::Matrix3d x_rot, y_rot, z_rot;

    x_rot << 1, 0, 0,
             0, std::cos(phi), -std::sin(phi),
             0, std::sin(phi),  std::cos(phi);

    y_rot << std::cos(theta), 0, std::sin(theta),
             0, 1, 0,
            -std::sin(theta), 0, std::cos(theta);

    z_rot << std::cos(psi), -std::sin(psi), 0,
             std::sin(psi),  std::cos(psi), 0,
             0, 0, 1;

    return z_rot * y_rot * x_rot;
}

// Inverse of the rotation matrix (R_b__n_inv)
Eigen::Matrix3d R_b__n_inv(double phi, double theta, double psi) {
    Eigen::Matrix3d R_inv;
    R_inv << std::cos(psi)*std::cos(theta), std::cos(theta)*std::sin(psi), -std::sin(theta),
             std::cos(psi)*std::sin(phi)*std::sin(theta) - std::cos(phi)*std::sin(psi),
             std::cos(phi)*std::cos(psi) + std::sin(phi)*std::sin(psi)*std::sin(theta),
             std::cos(theta)*std::sin(phi),
             std::sin(phi)*std::sin(psi) + std::cos(phi)*std::cos(psi)*std::sin(theta),
             std::cos(phi)*std::sin(psi)*std::sin(theta) - std::cos(psi)*std::sin(phi),
             std::cos(phi)*std::cos(theta);

    return R_inv;
}

// Transformation matrix for angular velocity (T)
Eigen::Matrix3d T(double phi, double theta) {
    Eigen::Matrix3d T_mat;
    T_mat << 1,     std::sin(phi)*std::tan(theta),      std::cos(phi)*std::tan(theta),
             0,     std::cos(phi),                      -std::sin(phi),
             0,     std::sin(phi)/std::cos(theta),      std::cos(phi)/std::cos(theta);
    return T_mat;
}

// Coriolis matrix (C)
Eigen::Matrix<double, 6, 6> C(const Eigen::Matrix<double, 6, 6>& M, const Eigen::Matrix<double, 6, 1>& nu) {
    int dimM = M.rows();
    int dimNu = nu.rows();

    Eigen::Matrix3d M11 = M.topLeftCorner(3, 3);
    Eigen::Matrix3d M12 = M.topRightCorner(3, 3);
    Eigen::Matrix3d M21 = M.bottomLeftCorner(3, 3);
    Eigen::Matrix3d M22 = M.bottomRightCorner(3, 3);

    Eigen::Vector3d nu1 = nu.head(3);
    Eigen::Vector3d nu2 = nu.tail(3);

    Eigen::Matrix<double, 6, 6> coriolis_mat;
    coriolis_mat << Eigen::Matrix3d::Zero(), -S(M11 * nu1 + M12 * nu2),
                    -S(M11 * nu1 + M12 * nu2), -S(M21 * nu1 + M22 * nu2);
    return coriolis_mat;
}

// Vector from CG to CB in body frame
Eigen::Vector3d r_gb__b(0, 0, r_z_gb__b);

// Added mass and inertia matrix (Initialized globally)
Eigen::Matrix<double, 6, 6> M_A_CB = Eigen::Matrix<double, 6, 6>::Zero();

// Aerodynamic damping matrix (Initialized globally)
Eigen::Matrix<double, 6, 6> D_CB = Eigen::Matrix<double, 6, 6>::Zero();

int main() {
    // Assign diagonal values to inertia matrix at CG
    M_RB_CG.diagonal() << m_RB, m_RB, m_RB, I_RBx, I_RBx, I_RBx;

    // Inertia matrix relative to the center of buoyancy (CB)
    Eigen::Matrix<double, 6, 6> M_RB_CB = H(r_gb__b).transpose() * M_RB_CG * H(r_gb__b);

    // Assign diagonal values to added mass matrix
    M_A_CB.diagonal() << 0.0466, 0.0466, 0.0545, 0.0, 0.0, 0.0;

    // Total inertia matrix at the center of buoyancy
    Eigen::Matrix<double, 6, 6> M_CB = M_RB_CB + M_A_CB;
    Eigen::Matrix<double, 6, 6> M_CB_inv = M_CB.inverse();

    // Gravitational force in the navigation frame
    const double g_acc = 9.8;  // Gravitational acceleration (m/s^2)
    Eigen::Vector3d fg_n = m_RB * Eigen::Vector3d(0, 0, g_acc);  // Force due to gravity

    // Assign diagonal values to aerodynamic damping matrix
    D_CB.diagonal() << 0.0125, 0.0125, 0.0480, 0.000862, 0.000862, 0.000862;

    // Print the blimp geometry and mass properties
    std::cout << "Height of envelope (Henv): " << Henv << std::endl;
    std::cout << "Height of gondola (Hgon): " << Hgon << std::endl;
    std::cout << "Distance from CG to CB (r_z_gb__b): " << r_z_gb__b << std::endl;
    std::cout << "Distance from CB to thrust generation point (r_z_tg__b): " << r_z_tg__b << std::endl;

    // Print mass and inertia properties
    std::cout << "Mass of the blimp (m_RB): " << m_RB << std::endl;
    std::cout << "Inertia matrix at CG (M_RB_CG):\n" << M_RB_CG << std::endl;
    std::cout << "Inertia matrix at CB (M_RB_CB):\n" << M_RB_CB << std::endl;
    std::cout << "Total inertia matrix at CB (M_CB):\n" << M_CB << std::endl;
    std::cout << "Inverse of total inertia matrix at CB (M_CB_inv):\n" << M_CB_inv << std::endl;

    // Print gravitational force
    std::cout << "Gravitational force (fg_n):\n" << fg_n << std::endl;

    // Print aerodynamic damping matrix
    std::cout << "Aerodynamic damping matrix (D_CB):\n" << D_CB << std::endl;

    // Test cross product operator (S operator)
    Eigen::Vector3d r(1, 2, 3);
    Eigen::Matrix3d S_r = S(r);
    std::cout << "S operator for vector r:\n" << S_r << std::endl;

    // Test rotation matrix R_b__n
    double phi = 0.1, theta = 0.2, psi = 0.3;  // Example Euler angles in radians
    Eigen::Matrix3d R_bn = R_b__n(phi, theta, psi);
    std::cout << "Rotation matrix (R_b__n):\n" << R_bn << std::endl;

    // Test inverse of the rotation matrix
    Eigen::Matrix3d R_bn_inv = R_b__n_inv(phi, theta, psi);
    std::cout << "Inverse rotation matrix (R_b__n_inv):\n" << R_bn_inv << std::endl;

    // Test angular velocity transformation matrix T
    Eigen::Matrix3d T_mat = T(phi, theta);
    std::cout << "Transformation matrix for angular velocity (T):\n" << T_mat << std::endl;

    // Test Coriolis matrix
    Eigen::Matrix<double, 6, 6> M = Eigen::Matrix<double, 6, 6>::Random();  // Random inertia matrix for testing
    Eigen::Matrix<double, 6, 1> nu = Eigen::Matrix<double, 6, 1>::Random();  // Random velocity vector
    Eigen::Matrix<double, 6, 6> coriolis_mat = C(M, nu);
    std::cout << "Coriolis matrix (C):\n" << coriolis_mat << std::endl;

    return 0;
}
