import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class LidarSub(Node):
    def __init__(self):
        super().__init__('simple_subscriber')
        self.stop = False
        self.subscription = self.create_subscription(LaserScan, '/scan', self.listener_callback, 10)

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.avoiding_obstacles)

    def avoiding_obstacles(self):
        data = Twist()
        if self.stop:
            data.linear.x = 0.0
        else:
            data.linear.x = 1.0
        self.publisher.publish(data)
        
    def listener_callback(self, msg):
        for i in range(90, 270):
            if min(msg.ranges[i], 100) < 2:
                self.stop = True
                break
            else:
                self.stop = False



# class VelocityPublisher(Node):
#     def __init__(self):
#         super().__init__('simple publisher')
#         self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

#     def avoiding_obstacles(self, msg):
#         msg = Vector3()
#         msg.linear.x = 1.0


def main(args=None):
    rclpy.init(args=args)

    lidar_subscriber = LidarSub()

    rclpy.spin(lidar_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    lidar_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

