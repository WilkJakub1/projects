# import RPi.GPIO as GPIO
import time

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16
from geometry_msgs.msg import Twist

class Pwm2vel(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subsriber_ = self.create_subscription(Twist, 'cmd_vel', self.driving, 10)

        # right_motor_a = 24
        # right_motor_b = 23
        # right_motor_en = 25
        # left_motor_a = 15
        # left_motor_b = 14
        # left_motor_en = 4

        # GPIO.setmode(GPIO.BCM)

        # GPIO.setup(right_motor_a, GPIO.OUT)
        # GPIO.setup(right_motor_b, GPIO.OUT)
        # GPIO.setup(right_motor_en, GPIO.OUT)

        # GPIO.setup(left_motor_a, GPIO.OUT)
        # GPIO.setup(left_motor_b, GPIO.OUT)
        # GPIO.setup(left_motor_en, GPIO.OUT)
        # self.rm_a = right_motor_a
        # self.rm_b = right_motor_b
        # self.rm_en = right_motor_en

        # self.lm_a = left_motor_a
        # self.lm_b = left_motor_b
        # self.lm_en = left_motor_en

        # pwm_r = GPIO.PWM(right_motor_en, 1000)
        # pwm_r.start(25)
        self.timer = 0.5
        self.subsriber_

    def driving(self, msg):
        if msg.linear.x > 0:
            print('jadziem')
            # GPIO.output(self.rm_a, GPIO.HIGH)
            # GPIO.output(self.rm_b, GPIO.LOW)
            # GPIO.output(self.lm_a, GPIO.HIGH)
            # GPIO.output(self.lm_b, GPIO.LOW)
        elif msg.linear.x < 0:
            print('cofanko')
            # GPIO.output(self.rm_a, GPIO.LOW)
            # GPIO.output(self.rm_b, GPIO.HIGH)
            # GPIO.output(self.lm_a, GPIO.LOW)
            # GPIO.output(self.lm_b, GPIO.HIGH)
        elif msg.angular.z < 0:
            print('prawo')
            # GPIO.output(self.rm_a, GPIO.LOW)
            # GPIO.output(self.rm_b, GPIO.HIGH)
            # GPIO.output(self.lm_a, GPIO.HIGH)
            # GPIO.output(self.lm_b, GPIO.LOW)
        elif msg.angular.z > 0:
            print('lewo')
            # GPIO.output(self.rm_a, GPIO.HIGH)
            # GPIO.output(self.rm_b, GPIO.LOW)
            # GPIO.output(self.lm_a, GPIO.LOW)
            # GPIO.output(self.lm_b, GPIO.HIGH)
        else:
            print('stoi nie opada')
            # GPIO.output(self.lm_b, GPIO.LOW)
            # GPIO.output(self.rm_a, GPIO.LOW)
            # GPIO.output(self.rm_b, GPIO.LOW)
            # GPIO.output(self.lm_a, GPIO.LOW)
        print(msg.linear.x)
        print(msg.angular.z)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = Pwm2vel()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

