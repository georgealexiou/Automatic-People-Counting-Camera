import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, utils, activations
from configs.arch import CNN_CONFIG
from math_utils import MathUtil


class Yolo:
    def __init__(self, s, stride=2, pool=2):
        self.stride = stride
        self.pool = pool
        self.math_util = MathUtil()
        self.s = s
        self.input_shape = (448, 448, 3)

    def create_darknet(self):

        darknet = models.Sequential()

        for i in CNN_CONFIG:

            if type(i) == tuple:
                if i == CNN_CONFIG[0]:
                    darknet.add(self.create_conv2d_layer(kernel_size=i[0], filters=i[1], strides=i[2],
                                                         input_shape=self.input_shape))
                else:
                    darknet.add(self.create_conv2d_layer(kernel_size=i[0], filters=i[1], strides=i[2]))

            elif type(i) == str:
                darknet.add(self.create_maxpool2d_layer(pool_size=2, strides=2))

            elif type(i) == list:
                for _ in range(i[2]):
                    darknet.add(self.create_conv2d_layer(kernel_size=i[0][0], filters=i[0][1], strides=i[0][2]))
                    darknet.add(self.create_conv2d_layer(kernel_size=i[1][0], filters=i[1][1], strides=i[1][2]))



        # Tired nonsene
        # S, B, C = split, num_boxes, 1

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

    def create_conv2d_layer(self, filters: int, kernel_size: int, strides: int, activation: MathUtil = MathUtil().leaky_relu(0.1),
                            input_shape: (int, int, int) = None) -> layers.Conv2D:
        if input_shape:
            return layers.Conv2D(
                filters,
                kernel_size=kernel_size,
                strides=strides,
                activation=activation,
                padding='same',
                input_shape=input_shape
            )
        else:
            return layers.Conv2D(
                filters,
                kernel_size=kernel_size,
                strides=strides,
                activation=activation,
                padding='same'
            )

    def create_maxpool2d_layer(self, pool_size: int, strides: int) -> layers.MaxPool2D:
        return layers.MaxPool2D(
            pool_size=pool_size,
            strides=strides,
            padding='same'
        )


if __name__ == "__main__":
    lol = Yolo(13)
    model = lol.create_darknet()
    model.summary()
