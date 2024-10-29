from setuptools import find_packages, setup

package_name = 'blimp_mpc_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mihir',
    maintainer_email='mihir@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'run_cbf_line       = blimp_mpc_ros.run_ctrl_cbf_line:main',
            'run_cbf_triangle   = blimp_mpc_ros.run_ctrl_cbf_triangle:main',
            # 'run_cbf_helix      = blimp_mpc_ros.run_ctrl_cbf_helix:main',

            'run_fbl_line       = blimp_mpc_ros.run_ctrl_fbl_line:main',
            'run_fbl_triangle   = blimp_mpc_ros.run_ctrl_fbl_triangle:main',
            'run_fbl_helix      = blimp_mpc_ros.run_ctrl_fbl_helix:main',

            'run_lqr_line       = blimp_mpc_ros.run_ctrl_lqr_line:main',
            'run_lqr_triangle   = blimp_mpc_ros.run_ctrl_lqr_triangle:main',
            'run_lqr_helix      = blimp_mpc_ros.run_ctrl_lqr_helix:main',

            'run_rta_box        = blimp_mpc_ros.run_ctrl_rta_box:main',
            
            # 'run_nlmpc_helix    = blimp_mpc_ros.run_ctrl_nlmpc_helix:main',
            'run_nlmpc_line     = blimp_mpc_ros.run_ctrl_nlmpc_line:main',
            'run_nlmpc_triangle = blimp_mpc_ros.run_ctrl_nlmpc_triangle:main',
            'run_nlmpc_rta      = blimp_mpc_ros.run_ctrl_nlmpc_rta:main',

            'run_blimp_data = blimp_mpc_ros.run_blimp_data:main',
            'state_node = blimp_mpc_ros.StateNode:main',

            'run_blimp_sim = blimp_mpc_ros.run_blimp_sim:main',

            'run_rta_sim = blimp_mpc_ros.run_rta_sim:main',


            'run_wardi_circle_horz = blimp_mpc_ros.x1_official_run_wardi_circle_horz:main',
            'run_wardi_circle_vert = blimp_mpc_ros.x2_official_run_wardi_circle_vert:main',
            'run_wardi_fig8_horz = blimp_mpc_ros.x3_official_run_wardi_fig8_horz:main',
            'run_wardi_fig8_vert_short = blimp_mpc_ros.x4_official_run_wardi_fig8_vert_short:main',
            'run_wardi_fig8_vert_tall = blimp_mpc_ros.x5_official_run_wardi_fig8_vert_tall:main',
            'run_wardi_circle_horz_spin = blimp_mpc_ros.x6_official_run_wardi_circle_horz_spin:main',
            'run_wardi_helix = blimp_mpc_ros.x7_official_run_wardi_helix:main',
            'run_wardi_helix_spin = blimp_mpc_ros.x8_official_run_wardi_helix_spin:main',


            'run_nlmpc_circle_horz = blimp_mpc_ros.y1_official_run_nlmpc_circle_horz:main',
            'run_nlmpc_circle_vert = blimp_mpc_ros.y2_official_run_nlmpc_circle_vert:main',
            'run_nlmpc_fig8_horz = blimp_mpc_ros.y3_official_run_nlmpc_fig8_horz:main',
            'run_nlmpc_fig8_vert_short = blimp_mpc_ros.y4_official_run_nlmpc_fig8_vert_short:main',
            'run_nlmpc_fig8_vert_tall = blimp_mpc_ros.y5_official_run_nlmpc_fig8_vert_tall:main',
            'run_nlmpc_circle_horz_spin = blimp_mpc_ros.y6_official_run_nlmpc_circle_horz_spin:main',
            'run_nlmpc_helix = blimp_mpc_ros.y7_official_run_nlmpc_helix:main',
            'run_nlmpc_helix_spin = blimp_mpc_ros.y8_official_run_nlmpc_helix_spin:main',

            'run_cbf_circle_horz = blimp_mpc_ros.z1_official_run_cbf_circle_horz:main',
            'run_cbf_circle_vert = blimp_mpc_ros.z2_official_run_cbf_circle_vert:main',
            'run_cbf_fig8_horz = blimp_mpc_ros.z3_official_run_cbf_fig8_horz:main',
            'run_cbf_fig8_vert_short = blimp_mpc_ros.z4_official_run_cbf_fig8_vert_short:main',
            'run_cbf_fig8_vert_tall = blimp_mpc_ros.z5_official_run_cbf_fig8_vert_tall:main',
            'run_cbf_circle_horz_spin = blimp_mpc_ros.z6_official_run_cbf_circle_horz_spin:main',
            'run_cbf_helix = blimp_mpc_ros.z7_official_run_cbf_helix:main',
            'run_cbf_helix_spin = blimp_mpc_ros.z8_official_run_cbf_helix_spin:main',

        ],
    },
)
