#!/usr/bin/env python

import RPi.GPIO as gpio
import time
import sys
import signal
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


def signal_handler(signal, frame): # ctrl + c -> exit program
        print('You pressed Ctrl+C!')
        sys.exit(0)


class DistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_publisher')
        self.publisher = self.create_publisher(Bool, 'distance_topic', 10)
        
        signal.signal(signal.SIGINT, signal_handler)
        gpio.setmode(gpio.BCM)

        self.stop = False

        self.trig = 20
        self.echo = 4
        gpio.setup(self.trig, gpio.OUT)
        gpio.setup(self.echo, gpio.IN)
        
        timer_period = 0.2
        self.timer = self.create_timer(timer_period, self.callback)
        self.i = 0

    def callback(self):
        gpio.output(self.trig, False)
        time.sleep(0.1)
        gpio.output(self.trig, True)
        time.sleep(0.00001)
        gpio.output(self.trig, False)
        pulse_start = time.time()
        while gpio.input(self.echo) == 0:
            pulse_star = time.time()
        while gpio.input(self.echo) == 1:
            pulse_end = time.time()
        if not pulse_end or pulse_end == pulse_start:
            pulse_end = pulse_start + 100
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        print(f"pulse_start = {pulse_start}")
        print(f"pulse_end = {pulse_end}")
        if pulse_duration >=0.01746:
            print('time out')
            
        elif distance > 300 or distance==0:
            print('out of range')
            
        distance = round(distance, 3) - 40
        if distance < 200:
            print ('Distance : %f cm'%distance)
        else:
            print('out of range')

        
        if distance < 20:
            self.stop = True
        else:
            self.stop = False

        msg = Bool()
        msg.data = self.stop
        self.publisher.publish(msg)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    distance_publisher = DistancePublisher()

    rclpy.spin(distance_publisher)

    distance_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
