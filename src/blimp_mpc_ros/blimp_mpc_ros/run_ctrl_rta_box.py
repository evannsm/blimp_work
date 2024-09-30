import rclpy

from . CtrlMPCBox import CtrlMPCBox
from . BlimpMPCNode import BlimpMPCNode

import sys

def main(args=sys.argv):
    print('Algorithm: FBL; trajectory: defined by RTA')

    if len(args) < 2:
        print("Please run with log file name as argument.")
        sys.exit(0)
    
    try:
        rclpy.init(args=args)

        dT = 0.05 # 40 Hz. #0.01 # 0.05 # 25 Hz, for now.
        rta_dT = 0.25#0.2
        controller = CtrlMPCBox(dT, rta_dT)
        node = BlimpMPCNode(controller, args[1])
        
        rclpy.spin(node)

    finally:
        node.destroy_node()

if __name__ == '__main__':
    main()
