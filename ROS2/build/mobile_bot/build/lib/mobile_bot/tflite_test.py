from tflite_runtime.interpreter import Interpreter
import tflite_runtime
import numpy as np
import os
import cv2

main_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
model_file = os.path.join(main_dir_path, 'data', 'lite-model_ssd_mobilenet_v1_100_320_uint8_nms_1.tflite')
input_file = os.path.join(main_dir_path, 'resources', 'asteroid_brown.png')

text_file = open("/home/jakub/ros2_ws/src/mobile_bot/data/labels.txt", "r")
label_array = text_file.readlines()


interpreter = Interpreter(model_path="/home/jakub/ros2_ws/src/mobile_bot/data/lite-model_ssd_mobilenet_v1_100_320_uint8_nms_1.tflite")

interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test the model on random input data.
camera_img = cv2.imread("/home/jakub/ros2_ws/src/mobile_bot/mobile_bot/person.jpg")
input_img = cv2.resize(camera_img, (320, 320))
input_img = input_img.reshape(1, input_img.shape[0], input_img.shape[1], input_img.shape[2])
input_img = input_img.astype(np.uint8)   

input_data = np.array(input_img, dtype=np.uint8)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

de_boxes = interpreter.get_tensor(output_details[0]['index'])[0]

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[1]['index'])

tflite.image.draw_bounding_boxes(
    images, boxes, colors, name=None
)

cv2.imshow('image', camera_img)
cv2.waitKey(0)
print(output_data)
print(label_array[int(output_data[0][0])])