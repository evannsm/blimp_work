import rclpy

from . BlimpMPCNode import BlimpMPCNode
from . xHardwareWardiHelixSpin import HardwareWardiHelixSpin
import sys

def main(args=sys.argv):
    print('Algorithm: Wardi controller; helix spinning trajectory. :)')

    if len(args) < 2:
        print("Please run with log file name as argument.")
        sys.exit(0)
    
    try:
        rclpy.init(args=args)

        dT = 0.025
        controller = HardwareWardiHelixSpin(dT)
        node = BlimpMPCNode(controller, args[1])
        
        rclpy.spin(node)

    finally:
        node.destroy_node()

if __name__ == '__main__':
    main()
