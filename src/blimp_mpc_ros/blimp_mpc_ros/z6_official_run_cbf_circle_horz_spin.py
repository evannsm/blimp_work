import rclpy

from . zHardwareCBFCircleHorzSpin import HardwareCBFCircleHorzSpin
from . BlimpMPCNode import BlimpMPCNode

import sys

def main(args=sys.argv):
    print('Algorithm: feedback linearization with CBFS; trajectory: circle horizontal spinning')

    if len(args) < 2:
        print("Please run with log file name as argument.")
        sys.exit(0)
    
    try:
        rclpy.init(args=args)

        dT = 0.025#0.05
        controller = HardwareCBFCircleHorzSpin(dT)
        node = BlimpMPCNode(controller, args[1])
        
        rclpy.spin(node)

    finally:
        node.destroy_node()

if __name__ == '__main__':
    main()
