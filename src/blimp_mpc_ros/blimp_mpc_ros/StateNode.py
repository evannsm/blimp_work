import rclpy
from rclpy.node import Node
import numpy as np
from nav_msgs.msg import Odometry

class StateNode(Node):
    def __init__(self, blimp_id=0):
        super().__init__('state_node')
        self.get_logger().info('StateNode started')

        # Load data from state_data.csv
        self.data = np.loadtxt('state_data.csv', delimiter=',', skiprows=3)
        self.dT = 0.01

        self.slow_dT = 0.4 # Slow enough so that the blimp finishes computing its RTA step.
        self.rta_dT = 0.2
        # Create a timer.
        self.create_timer(self.slow_dT, self.publish_state)
        self.c_index = int(15/0.01) # Discard the first 15 seconds of data.

        self.state_publisher = self.create_publisher(
            Odometry,
            f'/agents/blimp{blimp_id}/state',
            1
        )

    def publish_state(self):
        msg = Odometry()
        msg.header.stamp = self.get_clock().now().to_msg()

        msg.pose.pose.position.x = self.data[self.c_index, 7]
        msg.pose.pose.position.y = self.data[self.c_index, 8]
        msg.pose.pose.position.z = self.data[self.c_index, 9]

        msg.twist.twist.linear.x = self.data[self.c_index, 10]
        msg.twist.twist.linear.y = self.data[self.c_index, 11]
        msg.twist.twist.linear.z = self.data[self.c_index, 12]

        msg.twist.twist.linear.x = self.data[self.c_index, 1]
        msg.twist.twist.linear.y = self.data[self.c_index, 2]
        msg.twist.twist.linear.z = self.data[self.c_index, 3]

        msg.twist.twist.angular.x = self.data[self.c_index, 4]
        msg.twist.twist.angular.y = self.data[self.c_index, 5]
        msg.twist.twist.angular.z = self.data[self.c_index, 6]

        self.c_index += 1
        self.c_index += int(self.rta_dT/self.dT)

        self.state_publisher.publish(msg)

def main():
    rclpy.init()
    state_node = StateNode()
    rclpy.spin(state_node)
    state_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()