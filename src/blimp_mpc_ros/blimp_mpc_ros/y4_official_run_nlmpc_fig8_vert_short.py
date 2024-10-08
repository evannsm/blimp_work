import rclpy

from . yHardwareCasadiFig8VertShort import HardwareCasadiFig8VertShort
from . BlimpMPCNode import BlimpMPCNode

import sys

def main(args=sys.argv):
    print('Algorithm: NLMPC with Casadi; trajectory: fig8 vert short')

    if len(args) < 2:
        print("Please run with log file name as argument.")
        sys.exit(0)
    
    try:
        rclpy.init(args=args)

        dT = 0.04# 0.025
        controller = HardwareCasadiFig8VertShort(dT)
        node = BlimpMPCNode(controller, args[1])
        
        rclpy.spin(node)

    finally:
        node.destroy_node()

if __name__ == '__main__':
    main()
