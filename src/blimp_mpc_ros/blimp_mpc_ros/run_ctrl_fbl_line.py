import rclpy

from . CtrlFBLLine import CtrlFBLLine
from . BlimpMPCNode import BlimpMPCNode

import sys

def main(args=sys.argv):
    print('Algorithm: feedback linearization without CBFs; trajectory: line')

    if len(args) < 2:
        print("Please run with log file name as argument.")
        sys.exit(0)
    
    try:
        rclpy.init(args=args)

        dT = 0.05
        controller = CtrlFBLLine(dT)
        node = BlimpMPCNode(controller, args[1])
        
        rclpy.spin(node)

    finally:
        node.destroy_node()

if __name__ == '__main__':
    main()
