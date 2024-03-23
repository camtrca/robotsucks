# !user/bin/env python3

import rclpy
from rclpy.node import Node 
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped

class PathTracker(Node):
    def __init__(self):
        super().__init__('path_tracker')
        self.publisher = self.create_publisher(Path, 'robot_path', 10)
        self.create_subscription(
            PoseWithCovarianceStamped,
            '/pose',
            self.pose_callback,
            10)
        self.path = Path()

    def pose_callback(self,msg):
        print("Recording initiated")
        pose_stamped = PoseStamped()
        pose_stamped.header= msg.header
        pose_stamped.pose = msg.pose.pose
        
        self.path.poses.append(pose_stamped)
        self.path.header.stamp = self.get_clock().now().to_msg()
        self.path.header.fiirame_id = 'map'

        self.publisher.publish(self.path)
        print("Current recording segment finished")

def main(args=None):
    rclpy.init(args=args)
    node = PathTracker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__== '__main__':
    main() 