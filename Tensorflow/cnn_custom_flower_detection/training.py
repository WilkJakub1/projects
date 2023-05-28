import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
import random

data_dir = os.path.join(os.getcwd(), 'dataset')

labels=['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

dataset = []
for dir in os.listdir(data_dir):
    for img in os.listdir(os.path.join(data_dir, dir)):
        img_array = cv2.imread(os.path.join(data_dir,dir,img))
        img_array = cv2.resize(img_array, (200, 200))
        img_array = img_array/255.0

        dataset.append([img_array, labels.index(dir)])
    print(dir)

for i in range(100):
    print(dataset[0][0][0][i])

print(dataset[0])

plt.figure(figsize=(5, 5))
plt.imshow(dataset[0][0])   
plt.show()

random.shuffle(dataset)

Xtrain = list(image[0] for image in dataset[:-int(0.2*len(dataset))])
Ytrain = list(image[1] for image in dataset[:-int(0.2*len(dataset))])
Xval = list(image[0] for image in dataset[-int(0.2*len(dataset)):])
Yval = list(image[1] for image in dataset[-int(0.2*len(dataset)):])


Xtrain = np.array(Xtrain)
Ytrain = np.array(Ytrain)
Xval = np.array(Xval)
Yval = np.array(Yval)

print(Xtrain.shape)
print(Xval.shape)
print(set(Ytrain))
model = tf.keras.Sequential()

model.add(tf.keras.layers.Conv2D(32, 
                                 (3, 3), 
                                 activation='relu', 
                                 input_shape=(200, 200, 3)))
model.add(tf.keras.layers.MaxPool2D((2,2)))
model.add(tf.keras.layers.Conv2D(256, 3, activation='relu'))
model.add(tf.keras.layers.MaxPool2D())
model.add(tf.keras.layers.Conv2D(512, 3, activation='relu'))
model.add(tf.keras.layers.MaxPool2D((2, 2)))
model.add(tf.keras.layers.Conv2D(128, 3, activation='relu'))
model.add(tf.keras.layers.MaxPool2D((2, 2)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128))
model.add(tf.keras.layers.Dense(64))
model.add(tf.keras.layers.Dense(units=5))

model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

early_stopping = tf.keras.callbacks.EarlyStopping(monitor='accuracy', 
                                                  min_delta=0.01, 
                                                  patience=3, 
                                                  verbose=1)

model_checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath='model/best_modelv4.h5', 
                                                      monitor='accuracy', 
                                                      verbose=1, 
                                                      save_best_only=True)

cb = [early_stopping, model_checkpoint]

model.fit(Xtrain, Ytrain, batch_size=32, epochs=16, verbose=2, callbacks=cb, validation_data=(Xval, Yval))
model.history
