import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
import tensorflow as tf
import os
from tensorflow.keras.applications.vgg19 import preprocess_input
import numpy as np
import cv2

class ObjectDetector:
    def __init__(self):

        self.model_path = os.path.join(os.getcwd(), 'model/best_modelv3.h5')

        self.model = tf.keras.models.load_model(self.model_path)

        self.image_path = os.path.join(os.getcwd(), '/test_images/flower.jpg')

        self.classes = {0:'Daisy', 1:'Dandelion', 2:'Rose', 3:'Sunflower', 4:'Tulip'}

    def prediction(self, path):
        img_array = cv2.imread(path)
        img_array = cv2.resize(img_array, (200, 200))
        img_array = img_array/255.0
        # cv2.imshow('name', img_array)

        np.array(img_array)
        img_array = np.expand_dims(img_array, axis=0)
        # np.expand_dims(img_array, axis=0)
        print('\n\n-----------------------')
        print(img_array.shape)
        print('-----------------------\n\n')
        pred = self.model.predict(img_array)
        print(pred)
        
        return self.classes[np.argmax(pred)]

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
        QLabel{
            border: 10px dashed #333
            }
        '''
        )

    def setPixmap(self, image):
        super().setPixmap(image)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setAcceptDrops(True)
        self.detection = 'No object detected'

        self.object_detector = ObjectDetector()

        mainLayout = QVBoxLayout()

        self.photoViewer = ImageLabel()

        self.object = QLabel(f'{self.detection}')
        self.object.setFont(QFont('Times', 24, weight=QFont.Bold))

        mainLayout.addWidget(self.photoViewer)
        mainLayout.addWidget(self.object)

        self.setLayout(mainLayout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            # self.set_image(file_path)
            self.object.setText(self.object_detector.prediction(file_path))
        else:
            event.ignore()
    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))


app = QApplication(sys.argv)

demo = App()
demo.show()

sys.exit(app.exec_())