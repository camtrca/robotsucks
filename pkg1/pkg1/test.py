#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from find_object_2d.msg import ObjectsStamped 

class ObjectDetectionMover(Node):
    def __init__(self):
        super().__init__('object_detection_mover')
        # Initialize subscriber to the object detection topic
        self.subscription = self.create_subscription(
            ObjectsStamped,
            '/objectsStamped',
            self.detection_callback,
            10)
        self.get_logger().info("whatever")
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

    def detection_callback(self, msg):
        # self.get_logger().info('Object Detected: {}'.format(msg.objects.data))
        for i in msg.objects.data:
            try:
                if msg.objects.data[0] == 1:
                    self.get_logger().info("start detected")
                    break
            except:
                self.get_logger().error("nothing detected")

def main(args=None):
    rclpy.init(args=args)
    node = ObjectDetectionMover()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()