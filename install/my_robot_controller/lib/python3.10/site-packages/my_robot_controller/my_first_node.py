#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# My Node inherits from Node class
class MyNode(Node): 
    def __init__(self):
        # Define node name
        super().__init__("first_node")
        self.get_logger().info("HELLO FROM ROS2")

def main(args=None):
    # init ROS2 communications
    rclpy.init(args=args)
    # create node
    node = MyNode()

    # spin - node will be alive until you kill it
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
