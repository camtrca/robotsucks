import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from action_msgs.msg import GoalStatusArray
 
class TargetedExplorationController(Node):

    def __init__(self):
        super().__init__('targeted_exploration_controller')
        self.pose_publisher = self.create_publisher(PoseStamped, 'move_base_simple/goal', 10)
        self.status_subscriber = self.create_subscription(GoalStatusArray, 'move_base/status', self.status_callback, 10)
        self.targets = [(x, y) for x, y in [(2.0, 2.0), (4.0, 4.0)]]  # List of target coordinates
        self.current_target_index = 0
 
    def status_callback(self, msg):
        if msg.status_list and msg.status_list[-1].status == 3:  # Check if the goal was reached
            self.get_logger().info('Reached a target. Performing scan...')
            # Assume scanning is performed here
            self.current_target_index += 1
            if self.current_target_index < len(self.targets):
                self.send_goal_to_next_target()
 
    def send_goal_to_next_target(self):

        if self.current_target_index < len(self.targets):
            x, y = self.targets[self.current_target_index]
            goal = PoseStamped()
            goal.header.frame_id = "map"
            goal.pose.position.x = x
            goal.pose.position.y = y
            goal.pose.orientation.w = 1.0  # Proper orientation setting required
            self.pose_publisher.publish(goal)
            self.get_logger().info(f'Sending robot to next target: {x}, {y}')
 
    def start_exploration(self):
        self.send_goal_to_next_target()
 
def main(args=None):

    rclpy.init(args=args)
    controller = TargetedExplorationController()
    controller.start_exploration()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()
 
if __name__ == '__main__':

    main()
