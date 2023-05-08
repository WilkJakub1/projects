import cv2

img = cv2.imread('/home/jakub/ros2_ws/src/mobile_bot/mobile_bot/car.jpg')

classNames = []
classFile = '/home/jakub/ros2_ws/src/mobile_bot/mobile_bot/object_detection_classes_coco.txt'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = "/home/jakub/ros2_ws/src/mobile_bot/mobile_bot/Opencv_test/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt"
weightsPath = "/home/jakub/ros2_ws/src/mobile_bot/mobile_bot/Opencv_test/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

classIds, confs, bbox = net.detect(img, confThreshold=0.5)
print(classIds, bbox)

for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
    cv2.rectangle(img, box, color=(0, 255, 0))
    cv2.putText(img, classNames[classId-1].upper(), (box[0]+10, box[1]+30),
    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)


cv2.imshow("Output", img)

cv2.waitKey(0)