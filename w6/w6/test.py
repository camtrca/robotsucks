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
        self.get_logger().info('Object Detected: {}'.format(msg))
        for obejct in msg.objects:
            if obejct.id == 1 and object.x > 100:
                self.move_command.linear.x = -0.5
                self.move_command.angular.z = 0.0
                self.publisher.publish(self.move_command)
                break

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