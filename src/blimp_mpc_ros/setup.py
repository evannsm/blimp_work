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
            'run_cbf_helix      = blimp_mpc_ros.run_ctrl_cbf_helix:main',
            'run_fbl_line       = blimp_mpc_ros.run_ctrl_fbl_line:main',
            'run_fbl_triangle   = blimp_mpc_ros.run_ctrl_fbl_triangle:main',
            'run_fbl_helix      = blimp_mpc_ros.run_ctrl_fbl_helix:main',
            'run_lqr_line       = blimp_mpc_ros.run_ctrl_lqr_line:main',
            'run_lqr_triangle   = blimp_mpc_ros.run_ctrl_lqr_triangle:main',
            'run_lqr_helix      = blimp_mpc_ros.run_ctrl_lqr_helix:main',
            'run_rta_box        = blimp_mpc_ros.run_ctrl_rta_box:main',
            'run_nlmpc_helix    = blimp_mpc_ros.run_ctrl_nlmpc_helix:main',
            'run_nlmpc_line     = blimp_mpc_ros.run_ctrl_nlmpc_line:main',
            'run_nlmpc_triangle = blimp_mpc_ros.run_ctrl_nlmpc_triangle:main',
            'run_nlmpc_rta      = blimp_mpc_ros.run_ctrl_nlmpc_rta:main',
            'run_wardi_circle_horz = blimp_mpc_ros.run_wardi_circle_horz:main',
            'run_blimp_sim = blimp_mpc_ros.run_blimp_sim:main',
            'run_blimp_data = blimp_mpc_ros.run_blimp_data:main',
            'state_node = blimp_mpc_ros.StateNode:main',
        ],
    },
)
