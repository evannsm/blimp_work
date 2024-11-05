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

from . CtrlCasadiHelix import CtrlCasadiHelix
from . CtrlCasadiTriangle import CtrlCasadiTriangle

from . xHardwareWardiCircleHorz import HardwareWardiCircleHorz
from . xHardwareWardiCircleVert import HardwareWardiCircleVert
from . xHardwareWardiFig8Horz import HardwareWardiFig8Horz
from . xHardwareWardiFig8VertShort import HardwareWardiFig8VertShort
from . xHardwareWardiFig8VertTall import HardwareWardiFig8VertTall
from . xHardwareWardiCircleHorzSpin import HardwareWardiCircleHorzSpin
from . xHardwareWardiHelix import HardwareWardiHelix
from . xHardwareWardiHelixSpin import HardwareWardiHelixSpin

from . yHardwareCasadiCircleHorz import HardwareCasadiCircleHorz
from . yHardwareCasadiCircleVert import HardwareCasadiCircleVert
from . yHardwareCasadiFig8Horz import HardwareCasadiFig8Horz
from . yHardwareCasadiFig8VertShort import HardwareCasadiFig8VertShort
from . yHardwareCasadiFig8VertTall import HardwareCasadiFig8VertTall
from . yHardwareCasadiCircleHorzSpin import HardwareCasadiCircleHorzSpin
from . yHardwareCasadiHelix import HardwareCasadiHelix
from . yHardwareCasadiHelixSpin import HardwareCasadiHelixSpin

from . zHardwareCBFCircleHorz import HardwareCBFCircleHorz
from . zHardwareCBFCircleVert import HardwareCBFCircleVert
from . zHardwareCBFFig8Horz import HardwareCBFFig8Horz
from . zHardwareCBFFig8VertShort import HardwareCBFFig8VertShort
from . zHardwareCBFFig8VertTall import HardwareCBFFig8VertTall
from . zHardwareCBFCircleHorzSpin import HardwareCBFCircleHorzSpin
from . zHardwareCBFHelix import HardwareCBFHelix
from . zHardwareCBFHelixSpin import HardwareCBFHelixSpin

import numpy as np
import sys
import time

import rclpy
from rclpy.node import Node
from pyJoules.handler.csv_handler import CSVHandler
from pyJoules.device.rapl_device import RaplPackageDomain, RaplCoreDomain
from pyJoules.energy_meter import EnergyContext
sys.path.append('/home/<your_user>/anaconda3/envs/<env_name>/lib/python3.10/site-packages')

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
        'casadi_triangle' : CtrlCasadiTriangle,
        
        'hardware_wardi_circle_horz' : HardwareWardiCircleHorz,
        'hardware_wardi_circle_vert' : HardwareWardiCircleVert,
        'hardware_wardi_fig8_horz' : HardwareWardiFig8Horz,
        'hardware_wardi_fig8_vert_short' : HardwareWardiFig8VertShort,
        'hardware_wardi_fig8_vert_tall' : HardwareWardiFig8VertTall,
        'hardware_wardi_circle_horz_spin' : HardwareWardiCircleHorzSpin,
        'hardware_wardi_helix' : HardwareWardiHelix,
        'hardware_wardi_helix_spin' : HardwareWardiHelixSpin,

        'hardware_casadi_circle_horz' : HardwareCasadiCircleHorz,
        'hardware_casadi_circle_vert' : HardwareCasadiCircleVert,
        'hardware_casadi_fig8_horz' : HardwareCasadiFig8Horz,
        'hardware_casadi_fig8_vert_short' : HardwareCasadiFig8VertShort,
        'hardware_casadi_fig8_vert_tall' : HardwareCasadiFig8VertTall,
        'hardware_casadi_circle_horz_spin' : HardwareCasadiCircleHorzSpin,
        'hardware_casadi_helix' : HardwareCasadiHelix,
        'hardware_casadi_helix_spin' : HardwareCasadiHelixSpin,

        'hardware_cbf_circle_horz' : HardwareCBFCircleHorz,
        'hardware_cbf_circle_vert' : HardwareCBFCircleVert,
        'hardware_cbf_fig8_horz' : HardwareCBFFig8Horz,
        'hardware_cbf_fig8_vert_short' : HardwareCBFFig8VertShort,
        'hardware_cbf_fig8_vert_tall' : HardwareCBFFig8VertTall,
        'hardware_cbf_circle_horz_spin' : HardwareCBFCircleHorzSpin,
        'hardware_cbf_helix' : HardwareCBFHelix,
        'hardware_cbf_helix_spin' : HardwareCBFHelixSpin,

    }
        
    try:
        pyjoules_on = bool(int((input("Do you want to log energy consumption? (0/1): "))))
        if pyjoules_on:
            csv_handler = CSVHandler('z_fbl_CHS_energy.log')

        dT = 0.033 # 0.01
        ctrl_dT = dT #0.05
        ctrl_period = int(ctrl_dT / dT)
        ctrl_ctr = 0
        
        STOP_TIME = 25 #30
        PLOT_ANYTHING = True#False
        PLOT_WAVEFORMS = True#False

        WINDOW_TITLE = 'Nonlinear'

        Simulator = BlimpSim
        Controller = mapping[args[1]]
        
        print("Running blimp simulator: " + args[1])
        
        ## SIMULATION
        sim = Simulator(dT)
        sim.set_var('x', 0.8)
        sim.set_var('y', 0.)
        sim.set_var('z', -1.3)


        plotter = BlimpPlotter()
        plotter.init_plot(WINDOW_TITLE,
                waveforms=PLOT_WAVEFORMS,
                disable_plotting=(not PLOT_ANYTHING))
        
        ctrl = Controller(ctrl_dT)
        ctrl.init_sim(sim)
        sim.set_var('x', ctrl.traj_x[0])
        sim.set_var('y', ctrl.traj_y[0])
        sim.set_var('z', ctrl.traj_z[0])
        sim.set_var('psi', ctrl.traj_psi[0])

        x0 = sim.get_var('x')
        y0 = sim.get_var('y')
        z0 = sim.get_var('z')
        print(f"HERE: {x0 =}, {y0 =}, {z0 =}")
        u = ctrl.get_ctrl_action(sim) 

        for n in range(int(STOP_TIME / dT)):
            print("Time: " + str(round(n*dT, 2))) 
            sim.update_model(u)
            # print(f"{ctrl_ctr =}, {ctrl_period =}")
            ctrl_ctr += 1
            if ctrl_ctr > ctrl_period:
                print("Getting control action")
                if pyjoules_on:
                    with EnergyContext(handler=csv_handler, domains=[RaplPackageDomain(0), RaplCoreDomain(0)]):
                        u = ctrl.get_ctrl_action(sim)
                else:
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
        if pyjoules_on:
            csv_handler.save_data()
if __name__ == '__main__':
    main()
