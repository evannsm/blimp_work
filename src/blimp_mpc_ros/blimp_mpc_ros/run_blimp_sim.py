from . BlimpSim import BlimpSim
from . BlimpPlotter import BlimpPlotter
from . BlimpLogger import BlimpLogger

from . CtrlCBFLine import CtrlCBFLine
from . CtrlCBFTriangle import CtrlCBFTriangle
from . CtrlCBFHelix import CtrlCBFHelix

from . CtrlFBLLine import CtrlFBLLine
from . CtrlFBLTriangle import CtrlFBLTriangle
from . CtrlFBLHelix import CtrlFBLHelix

from . CtrlLQRLine import CtrlLQRLine
from . CtrlLQRTriangle import CtrlLQRTriangle
from . CtrlLQRHelix import CtrlLQRHelix

from . CtrlMPCLine import CtrlMPCLine
from . CtrlMPCBox import CtrlMPCBox

from . CtrlWardiLine import CtrlWardiLine
from . CtrlWardiHelix import CtrlWardiHelix
from . CtrlWardiTriangle import CtrlWardiTriangle
from . CtrlWardiCircle import CtrlWardiCircle
from . CtrlWardiCircleYaw import CtrlWardiCircleYaw

from . CtrlCasadiHelix import CtrlCasadiHelix

from . HardwareWardiCircleVert import HardwareWardiCircleVert
from . HardwareWardiCircleHorz import HardwareWardiCircleHorz
from . HardwareWardiFig8Horz import HardwareWardiFig8Horz
from . HardwareWardiFig8VertShort import HardwareWardiFig8VertShort
from . HardwareWardiFig8VertTall import HardwareWardiFig8VertTall
from . HardwareWardiCircleYaw import HardwareWardiCircleYaw
from . HardwareWardiSpiralStairs import HardwareWardiSpiralStairs
import numpy as np
import sys
import time

import rclpy
from rclpy.node import Node


def main(args=sys.argv):
    if len(args) < 3:
        print("Please run with controller and log file name as arguments.")
        sys.exit(0)
        
    mapping = {
        'cbf_line': CtrlCBFLine,
        'cbf_triangle': CtrlCBFTriangle,
        'cbf_helix': CtrlCBFHelix,
        'fbl_line': CtrlFBLLine,
        'fbl_triange': CtrlFBLTriangle,
        'fbl_helix': CtrlFBLHelix,
        'lqr_line': CtrlLQRLine,
        'lqr_triangle': CtrlLQRTriangle,
        'lqr_helix': CtrlLQRHelix,
        'mpc_line': CtrlMPCLine,
        'rta_box': CtrlMPCBox,
        'casadi_helix': CtrlCasadiHelix,
        'wardi_line' : CtrlWardiLine,
        'wardi_helix' : CtrlWardiHelix,
        'wardi_triangle' : CtrlWardiTriangle,
        'wardi_circle' : CtrlWardiCircle,
        'hardware_wardi_circle_vert' : HardwareWardiCircleVert,
        'hardware_wardi_circle_horz' : HardwareWardiCircleHorz,
        'hardware_wardi_fig8_horz' : HardwareWardiFig8Horz,
        'hardware_wardi_fig8_vert_short' : HardwareWardiFig8VertShort,
        'hardware_wardi_fig8_vert_tall' : HardwareWardiFig8VertTall,
        'hardware_wardi_circle_yaw' : HardwareWardiCircleYaw,
        'hardware_wardi_spiral_stairs' : HardwareWardiSpiralStairs,


    }
        
    try:
        dT = 0.01
        ctrl_dT = dT
        # ctrl_dT = 0.05 #
        ctrl_period = int(ctrl_dT / dT)
        
        ctrl_ctr = 0
        
        STOP_TIME = 45 #30
        PLOT_ANYTHING = True#False
        PLOT_WAVEFORMS = True#False

        WINDOW_TITLE = 'Nonlinear'

        Simulator = BlimpSim
        Controller = mapping[args[1]]
        
        print("Running blimp simulator: " + args[1])
        
        ## SIMULATION
        print('here')
        sim = Simulator(dT)

        print('there')
        # print("1")
        plotter = BlimpPlotter()
        plotter.init_plot(WINDOW_TITLE,
                waveforms=PLOT_WAVEFORMS,
                disable_plotting=(not PLOT_ANYTHING))
        # print("2")
        ctrl = Controller(ctrl_dT)
        # print("3")
        ctrl.init_sim(sim)

        # print(f"{ctrl.traj_x[0] =}")
        sim.set_var('x', ctrl.traj_x[0])
        sim.set_var('y', ctrl.traj_y[0])
        sim.set_var('z', ctrl.traj_z[0])
        sim.set_var('psi', ctrl.traj_psi[0])

        # print("4")
        u = ctrl.get_ctrl_action(sim) 
        # print(u.shape) 
        for n in range(int(STOP_TIME / dT)):
            print("Time: " + str(round(n*dT, 2))) 
            sim.update_model(u)
            # print(f"{ctrl_ctr =}, {ctrl_period =}")
            ctrl_ctr += 1
            if ctrl_ctr > ctrl_period:
                print("Getting control action")
                u = ctrl.get_ctrl_action(sim)
                # print(u.shape) 
                ctrl_ctr = 0
            
            # print(f"input: {u}")
            # print(f"Current state: {round(sim.get_var('x'), 6)}, {round(sim.get_var('y'), 6)}, {round(sim.get_var('z'), 6)}, {round(sim.get_var('psi'), 6)}")
            # print(f"Control: {round(u[0].item(), 6)}, {round(u[1].item(), 6)}, {round(u[2].item(), 6)}, {round(u[3].item(), 6)}")


            # plotter.update_plot(sim)
            
            if plotter.window_was_closed():
                raise KeyboardInterrupt()
    except Exception as e:
        print(f'[ERROR] {e}')
        # Print the traceback
        import traceback
        traceback.print_exc()

    finally:
        print("Logging to logs/" + args[2])
        logger = BlimpLogger(args[2])
        logger.log(sim, ctrl)

if __name__ == '__main__':
    main()
