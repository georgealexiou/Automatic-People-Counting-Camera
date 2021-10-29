import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, utils, activations
from configs.arch import CNN_CONFIG
from math_utils import MathUtil



from keras.layers import Activation
from keras import backend as K
from keras.utils.generic_utils import get_custom_objects



# model = models.Sequential()
# model.add(layers.Conv2D(32, kernel_size=(3,3), activation="relu", input_shape=(28, 28, 1)))
# model.add(layers.MaxPooling2D(pool_size=(2,2)))
# model.add(layers.Conv2D(64, kernel_size=(3,3), activation="relu"))
# model.add(layers.MaxPooling2D(pool_size = (2,2)))
# model.add(layers.Conv2D(64, kernel_size=(3,3), activation="relu"))
# model.add(layers.Flatten())
# model.add(layers.Dropout(0.5))
# model.add(layers.Dense(num_classes, activation="softmax"))----------

from keras import backend as K

def custom_activation(x):
    return (K.sigmoid(x) * 5) - 1

# model.add(Dense(32 , activation=custom_activation))

class Yolo:
    def __init__(self, stride=2, pool=2):
        self.stride = stride
        self.pool = pool
        self.math_util = MathUtil()
    
    def create_arch(self):
        darknet = models.Sequential()
        
        darknet.add(
            layers.Conv2D(
                64, 
                kernel_size=(7,7),
                strides=(2, 2), 
                activation=self.math_util.leaky_relu(0.1),
                padding='same',
                input_shape=(448, 448, 3))
            )
        darknet.add(
            layers.MaxPool2D(
                pool_size=(2,2),
                strides=2, 
                padding='same')
            )
        
        for _ in range(4):
            print("IOUVY")
            


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