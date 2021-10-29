import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, utils
from configs.arch import CNN_CONFIG

# model = models.Sequential()
# model.add(layers.Conv2D(32, kernel_size=(3,3), activation="relu", input_shape=(28, 28, 1)))
# model.add(layers.MaxPooling2D(pool_size=(2,2)))
# model.add(layers.Conv2D(64, kernel_size=(3,3), activation="relu"))
# model.add(layers.MaxPooling2D(pool_size = (2,2)))
# model.add(layers.Conv2D(64, kernel_size=(3,3), activation="relu"))
# model.add(layers.Flatten())
# model.add(layers.Dropout(0.5))
# model.add(layers.Dense(num_classes, activation="softmax"))

class Yolo(object):
    def __init__(self, stride=2, activation=0.1, pool=2):
        self.stride = stride
        self.activation = activation
        self.pool = pool
    
    def create_arch(self):
        darknet = models.Sequential()
        darknet.add(layers.Conv2D(32, kernel_size=(3,3), activation="relu", input_shape=(28, 28, 1)))
        print(self.stride)
        darknet.summary()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()
        # darknet.add()

        return darknet 


if __name__ == "__main__":
    lol = Yolo()
    lol.create_arch()