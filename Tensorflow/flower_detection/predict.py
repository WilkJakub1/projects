import tensorflow as tf
import os
import matplotlib.pyplot as plt
from tensorflow.keras.applications.vgg19 import preprocess_input
import numpy as np

model_path = os.path.join(os.getcwd(), 'model/best_model.h5')
model = tf.keras.models.load_model(model_path)

image_path = os.path.join(os.getcwd(), '/test_images/flower.jpg')

classes = {0:'daisy', 1:'dandelion', 2:'rose', 3:'sunflower', 4:'tulip'}

def prediction(path, model, classes):
    image = tf.keras.utils.load_img(path, target_size=(320, 240))
    image = tf.keras.utils.img_to_array(image)
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    pred = model.predict(image)
    print(classes[np.argmax(pred)])
print(image_path)
prediction('/home/jakub/python/flower_detection/test_images/dandelion.jpg', model, classes)