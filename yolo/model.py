import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, utils, activations
from configs.arch import CNN_CONFIG
from math_utils import MathUtil



from keras.layers import Activation
from keras import backend as K
from keras.utils.generic_utils import get_custom_objects


class Yolo:
    def __init__(self, s, stride=2, pool=2):
        self.stride = stride
        self.pool = pool
        self.math_util = MathUtil()
        self.s = s
    
    def create_arch(self):
        
        darknet = models.Sequential()
        darknet.add(
            layers.Conv2D(
                64, 
                kernel_size=(7,7),
                strides=self.stride, 
                activation=self.math_util.leaky_relu(0.1),
                padding='same',
                input_shape=(448, 448, 3)
            )
        )
        darknet.add(
            layers.MaxPool2D(
                pool_size=(2,2),
                strides=self.stride, 
                padding='same'
            )
        )
        
        #https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization
        
        darknet.add(
            layers.Conv2D(
                192, 
                kernel_size=(3,3),
                activation=self.math_util.leaky_relu(0.1),
                padding='same',
                input_shape=(112, 112, 192)
            )
        )
        darknet.add(
            layers.MaxPool2D(
                pool_size=(2,2),
                strides=self.stride, 
                padding='same'
            )
        )



        darknet.add(
            layers.Conv2D(
                128, 
                kernel_size=(1,1),
                activation=self.math_util.leaky_relu(0.1),
                input_shape=(56, 56, 256)
            )
        )
        darknet.add(
            layers.Conv2D(
                256, 
                kernel_size=(3,3),
                activation=self.math_util.leaky_relu(0.1),
                padding='same',
                input_shape=(56, 56, 256)
            )
        )
        darknet.add(
            layers.Conv2D(
                256, 
                kernel_size=(1,1),
                activation=self.math_util.leaky_relu(0.1),
                input_shape=(56, 56, 256)
            )
        )
        darknet.add(
            layers.Conv2D(
                512, 
                kernel_size=(3,3),
                activation=self.math_util.leaky_relu(0.1),
                padding='same',
                input_shape=(56, 56, 256)
            )
        )
        darknet.add(
            layers.MaxPool2D(
                pool_size=(2,2),
                strides=self.stride, 
                padding='same'
            )
        )

        for _ in range(4):
            darknet.add(
                layers.Conv2D(
                    256, 
                    kernel_size=(1,1),
                    activation=self.math_util.leaky_relu(0.1),
                    input_shape=(28, 28, 512)
                )
            )
            darknet.add(
                layers.Conv2D(
                    512, 
                    kernel_size=(3,3),
                    activation=self.math_util.leaky_relu(0.1),
                    padding='same',
                    input_shape=(28, 28, 512)
                )
            )
        darknet.add(
            layers.Conv2D(
                512, 
                kernel_size=(1,1),
                activation=self.math_util.leaky_relu(0.1),
                input_shape=(28, 28, 512)
            )
        )
        darknet.add(
            layers.Conv2D(
                1024, 
                kernel_size=(3,3),
                activation=self.math_util.leaky_relu(0.1),
                padding='same',
                input_shape=(28, 28, 512)
            )
        )
        darknet.add(
            layers.MaxPool2D(
                pool_size=(2,2),
                strides=self.stride, 
                padding='same'
            )
        )



        for _ in range(2):
            darknet.add(
                layers.Conv2D(
                    512, 
                    kernel_size=(1,1),
                    activation=self.math_util.leaky_relu(0.1),
                    input_shape=(14, 14, 1024)
                )
            )
            darknet.add(
                layers.Conv2D(
                    1024, 
                    kernel_size=(3,3),
                    activation=self.math_util.leaky_relu(0.1),
                    padding='same',
                    input_shape=(14, 14, 1024)
                )
            )
        darknet.add(
            layers.Conv2D(
                1024, 
                kernel_size=(3,3),
                activation=self.math_util.leaky_relu(0.1),
                padding='same',
                input_shape=(14, 14, 1024)
            )
        )
        darknet.add(
            layers.Conv2D(
                1024, 
                kernel_size=(3,3),
                strides=self.stride, 
                activation=self.math_util.leaky_relu(0.1),
                padding='same',
                input_shape=(14, 14, 1024)
            )
        )



        darknet.add(
            layers.Conv2D(
                1024, 
                kernel_size=(3,3),
                activation=self.math_util.leaky_relu(0.1),
                padding='same',
                input_shape=(7, 7, 1024)
            )
        )
        darknet.add(
            layers.Conv2D(
                1024, 
                kernel_size=(3,3),
                activation=self.math_util.leaky_relu(0.1),
                padding='same',
                input_shape=(7, 7, 1024)
            )
        )

        # Tired nonsene
        S, B, C = split, num_boxes, 1

        # tf.keras.layers.Dense(
        #     units,
        #     activation=None,
        #     use_bias=True,
        #     kernel_initializer="glorot_uniform",
        #     bias_initializer="zeros",
        #     kernel_regularizer=None,
        #     bias_regularizer=None,
        #     activity_regularizer=None,
        #     kernel_constraint=None,
        #     bias_constraint=None,
        #     **kwargs
        # )


        return darknet 


if __name__ == "__main__":
    lol = Yolo()
    model = lol.create_arch()
    model.summary()