import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

import argparse
import sys
import time

from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import utils


class CameraSub(Node):
    def __init__(self):
        super().__init__('simple_subscriber')
        self.subscription = self.create_subscription(Image, '/camera/image_raw', self.listener_callback, 10)
        self.bridge = CvBridge()
        self.frame = 0

        self.turn_right = False
        self.turn_left = False
        self.forward = False

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.parser.add_argument(
            '--model',
            help='Path of the object detection model.',
            required=False,
            default='efficientdet_lite0.tflite')
        self.parser.add_argument(
            '--cameraId', help='Id of camera.', required=False, type=int, default=2)
        self.parser.add_argument(
            '--frameWidth',
            help='Width of frame to capture from camera.',
            required=False,
            type=int,
            default=640)
        self.parser.add_argument(
            '--frameHeight',
            help='Height of frame to capture from camera.',
            required=False,
            type=int,
            default=480)
        self.parser.add_argument(
            '--numThreads',
            help='Number of CPU threads to run the model.',
            required=False,
            type=int,
            default=4)
        self.parser.add_argument(
            '--enableEdgeTPU',
            help='Whether to run the model on EdgeTPU.',
            action='store_true',
            required=False,
            default=False)
        self.args = self.parser.parse_args()

        self.model = self.args.model
        self.camera_id = int(self.args.cameraId)
        self.width = self.args.frameWidth
        self.height = self.args.frameHeight
        self.num_threads = int(self.args.numThreads)
        self.enable_edgetpu = bool(self.args.enableEdgeTPU)

        self.row_size = 20  # pixels
        self.left_margin = 24  # pixels
        self.text_color = (0, 0, 255)  # red
        self.font_size = 1
        self.font_thickness = 1
        self.fps_avg_frame_count = 10

        # Initialize the object detection model
        self.base_options = core.BaseOptions(
            file_name=self.model, use_coral=self.enable_edgetpu, num_threads=self.num_threads)
        self.detection_options = processor.DetectionOptions(
            max_results=3, score_threshold=0.3)
        self.options = vision.ObjectDetectorOptions(
            base_options=self.base_options, detection_options=self.detection_options)
        self.detector = vision.ObjectDetector.create_from_options(self.options)
        # self.file_path = '/home/jakub/.local/lib/python3.8/site-packages/tensorflow_lite_support/python/task/vision/efficientdet_lite0.tflite'
        # self.detector = vision.ObjectDetector.create_from_file(self.file_path)

        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.avoiding_obstacles)

    def avoiding_obstacles(self):
        data = Twist()
        if self.turn_right:
            data.angular.z = -0.1
        elif self.turn_left:
            data.angular.z = 0.1
        else:
            data.angular.z = 0.0
        if self.forward:
            data.linear.x = 0.2
        else:
            data.linear.x = 0.0
        self.publisher.publish(data)

    def listener_callback(self, msg):
        self.frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

        """Continuously run inference on images acquired from the camera.

        Args:
            model: Name of the TFLite object detection model.
            camera_id: The camera id to be passed to OpenCV.
            width: The width of the frame captured from the camera.
            height: The height of the frame captured from the camera.
            num_threads: The number of CPU threads to run the model.
            enable_edgetpu: True/False whether the model is a EdgeTPU model.
        """



        # Variables to calculate FPS
        counter, fps = 0, 0
        start_time = time.time()

        # Start capturing video input from the camera
        cap = cv2.VideoCapture(int(self.args.cameraId))
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.args.frameWidth,)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.args.frameHeight,)
        success, image = cap.read()
        image = cv2.flip(image, 1)
        # Visualization parameters

        # Continuously capture images from the camera and run inference
        # counter += 1
        # image = cv2.flip(self.frame, 1)

        # Convert the image from BGR to RGB as required by the TFLite model.
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Create a TensorImage object from the RGB image.
        input_tensor = vision.TensorImage.create_from_array(rgb_image)

        # Run object detection estimation using the model.
        detection_result = self.detector.detect(input_tensor)

        for detection in detection_result.detections:
            if detection.categories[0].category_name == 'person':
                if (detection.bounding_box.width/2) + detection.bounding_box.origin_x < 200:
                    print('left\n\n') 
                    self.turn_right = True
                elif (detection.bounding_box.width/2) + detection.bounding_box.origin_x > 400:
                    print('right\n\n')
                    self.turn_left = True
                else:
                    print('middle\n\n')
                    self.turn_right = False
                    self.turn_left = False
                print(detection.bounding_box)
                if detection.bounding_box.width*detection.bounding_box.height > 150000:
                    self.forward = False
                else:
                    self.forward = True
                break
        else:
            self.turn_right = False
            self.turn_left = False
            self.forward = False


        # Draw keypoints and edges on input image
        image = utils.visualize(image, detection_result)

        # Calculate the FPS
        if counter % self.fps_avg_frame_count == 0:
            end_time = time.time()
            fps = self.fps_avg_frame_count / (end_time - start_time)
            start_time = time.time()

        # Show the FPS
        fps_text = 'FPS = {:.1f}'.format(fps)
        text_location = (self.left_margin, self.row_size)
        cv2.putText(image, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                    self.font_size, self.text_color, self.font_thickness)

        # Stop the program if the ESC key is pressed.
        cv2.imshow('object_detector', image)
        cv2.waitKey(50)







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

