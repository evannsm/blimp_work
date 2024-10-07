import rclpy

from . BlimpMPCNode import BlimpMPCNode
from . xHardwareWardiFig8VertShort import HardwareWardiFig8VertShort
import sys

def main(args=sys.argv):
    print('Algorithm: Wardi controller; fig8 vert short trajectory. :)')

    if len(args) < 2:
        print("Please run with log file name as argument.")
        sys.exit(0)
    
    try:
        rclpy.init(args=args)

        dT = 0.025
        controller = HardwareWardiFig8VertShort(dT)
        node = BlimpMPCNode(controller, args[1])
        
        rclpy.spin(node)

    finally:
        node.destroy_node()

if __name__ == '__main__':
    main()
