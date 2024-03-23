#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from rclpy.time import Time
import tf2_ros
import geometry_msgs.msg

class RobotPositionNode(Node):
    def __init__(self):
        super().__init__('robot_position_node')
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(5.0, self.timer_callback)  # Call timer_callback every 5 seconds

    def timer_callback(self):
        try:
            transform = self.tf_buffer.lookup_transform('map', 'base_link', Time())
            position = transform.transform.translation
            print(f"Robot's Position in Map Coordinates: {position.x}, {position.y}, {position.z}")
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            self.get_logger().error(f'Error in transforming robot position: {str(e)}')
def main():
    rclpy.init()
    node = RobotPositionNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
    exit(0)
