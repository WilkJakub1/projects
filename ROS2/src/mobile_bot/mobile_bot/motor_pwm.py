import RPi.GPIO as GPIO
import time

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class Pwm2vel(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subsriber_ = self.create_subscription(Twist, 'cmd_vel', self.driving, 10)
        
        self.distance_subscriber = self.create_subscription(Bool, 'distance_topic', self.distance, 10)

        self.stop = False

        right_motor_a = 17
        right_motor_b = 27
        right_motor_en = 25
        left_motor_a = 23
        left_motor_b = 24
        left_motor_en = 4

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(right_motor_a, GPIO.OUT)
        GPIO.setup(right_motor_b, GPIO.OUT)
        GPIO.setup(right_motor_en, GPIO.OUT)

        GPIO.setup(left_motor_a, GPIO.OUT)
        GPIO.setup(left_motor_b, GPIO.OUT)
        GPIO.setup(left_motor_en, GPIO.OUT)
        self.rm_a = right_motor_a
        self.rm_b = right_motor_b
        self.rm_en = right_motor_en

        self.lm_a = left_motor_a
        self.lm_b = left_motor_b
        self.lm_en = left_motor_en

        self.pwm_r = GPIO.PWM(self.rm_en, 1000)
        self.pwm_l = GPIO.PWM(self.lm_en, 1000)
        self.pwm_r.start(50)
        self.pwm_l.start(50)
        self.timer = 0.1
        self.subsriber_

    def distance(self, msg):
        self.stop = msg.data

    def driving(self, msg):
        self.pwm_r.ChangeDutyCycle(100)
        self.pwm_l.ChangeDutyCycle(100)
#        if msg.linear.x > 0:
#            print('jadziem')
#            GPIO.output(self.rm_a, GPIO.HIGH)
#            GPIO.output(self.rm_b, GPIO.LOW)
#            GPIO.output(self.lm_a, GPIO.HIGH)
#            GPIO.output(self.lm_b, GPIO.LOW)
#        elif msg.linear.x < 0:
#            print('cofanko')
#            GPIO.output(self.rm_a, GPIO.LOW)
#            GPIO.output(self.rm_b, GPIO.LOW)
#            GPIO.output(self.lm_a, GPIO.LOW)
#            GPIO.output(self.lm_b, GPIO.LOW)
        if msg.angular.z < 0 and not self.stop:
            print('prawo')
            GPIO.output(self.rm_a, GPIO.LOW)
            GPIO.output(self.rm_b, GPIO.HIGH)
            GPIO.output(self.lm_a, GPIO.LOW)
            GPIO.output(self.lm_b, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(self.rm_b, GPIO.LOW)
           # time.sleep(0.1)
 #           self.pwm_l.ChangeDutyCycle(0)
#            self.pwm_r.ChangeDutyCycle(0)
        elif msg.angular.z > 0 and not self.stop:
            print('lewo')
            GPIO.output(self.lm_a, GPIO.LOW)
            GPIO.output(self.lm_b, GPIO.HIGH)
            GPIO.output(self.rm_a, GPIO.LOW)
            GPIO.output(self.rm_b, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(self.lm_b, GPIO.LOW)
            #time.sleep(0.1)
        elif msg.linear.x > 0 and not self.stop:
            #self.pwm_l.ChangeDutyCycle(100)
            self.pwm_r.ChangeDutyCycle(90)
            GPIO.output(self.rm_a, GPIO.HIGH)
            GPIO.output(self.rm_b, GPIO.LOW)
            GPIO.output(self.lm_a, GPIO.HIGH)
            GPIO.output(self.lm_b, GPIO.LOW)
            print('prosto')
            self.pwm_l.ChangeDutyCycle(100)
            #self.pwm_r.ChangeDutyCycle(90)
            time.sleep(0.1)
      # elif msg.linear.x < 0:
       #     GPIO.output(self.rm_a, GPIO.LOW)
        #    GPIO.output(self.rm_b, GPIO.HIGH)
         #   GPIO.output(self.lm_a, GPIO.LOW)
          #  GPIO.output(self.lm_b, GPIO.HIGH)
           # print('tyl')
            #self.pwm_l.ChangeDutyCycle(100)
            #time.sleep(0.1)
            #GPIO.output(self.rm_b, GPIO.LOW)
            #GPIO.output(self.lm_b, GPIO.LOW)
        else:
            self.pwm_r.ChangeDutyCycle(0)
            self.pwm_l.ChangeDutyCycle(0)
   #         self.pwm_r.ChangeDutyCycle(0)
  #          self.pwm_l.ChangeDutyCycle(0)
 #           self.pwm_r.ChangeDutyCycle(0)
#            self.pwm_l.ChangeDutyCycle(0)
        print(msg.linear.x)
        print(msg.angular.z)
        if self.stop:
            print('stop')

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

