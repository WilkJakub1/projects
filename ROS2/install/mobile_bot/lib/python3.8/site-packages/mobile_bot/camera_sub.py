import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np


class CameraSub(Node):
    def __init__(self):
        super().__init__('simple_subscriber')
        self.subscription = self.create_subscription(Image, '/camera/image_raw', self.listener_callback, 10)
        self.bridge = CvBridge()
        self.frame = 0

    def listener_callback(self, msg):
        self.frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        cv2.imshow("Frame", self.frame)
        cv2.waitKey(20)



# class VelocityPublisher(Node):
#     def __init__(self):
#         super().__init__('simple publisher')
#         self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

#     def avoiding_obstacles(self, msg):
#         msg = Vector3()
#         msg.linear.x = 1.0


def main(args=None):
    rclpy.init(args=args)

    camera_subscriber = CameraSub()

    rclpy.spin(camera_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    camera_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

