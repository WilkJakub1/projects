This directory contains nodes for:

-object detection (person_follow.py)
-motors control (motor_pwm.py)
-ultrasonic sensor (sonar_sensor.py)


Detecting objects and sending detected person coordinates to node reponsible for controlling motors connected to Raspberry Pi 4 is hadled by person_follow.py. It also contains node for ultrasonic sensor that has higher priority and is able to stop motors in case robot gets too close to obstacle so that it avoids collision. 

Object detection node is based on example from: https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection/raspberry_pi and implemented into ROS 2 publisher node.