import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, utils, activations
from configs.arch import CNN_CONFIG, INPUT_CONFIG
from math_utils import MathUtil



class Yolo:
    def __init__(self, s, stride=2, pool=2):
        self.stride = stride
        self.pool = pool
        self.math_util = MathUtil()

    def create_darknet(self):

        darknet = models.Sequential()

        for i in CNN_CONFIG:
            # Create new convolutional Layer
            if type(i) == tuple:
                darknet.add(self.create_conv2d_layer(kernel_size=i[0], filters=i[1], strides=i[2]))

            # Create input layer
            elif type(i) == str and i == "INPUT_LAYER":
                darknet.add(self.create_input_layer())

            # Create maxpool layer
            elif type(i) == str and i == "MAX_POOL":
                darknet.add(self.create_maxpool2d_layer(pool_size=2, strides=2))

            # Multiple convolutional layer creation
            elif type(i) == list:
                for _ in range(i[2]):
                    darknet.add(self.create_conv2d_layer(kernel_size=i[0][0], filters=i[0][1], strides=i[0][2]))
                    darknet.add(self.create_conv2d_layer(kernel_size=i[1][0], filters=i[1][1], strides=i[1][2]))
        
        # Flatten, FCL, OPL
        darknet.add(layers.Flatten())
        darknet.add(layers.Dense(units=4096))
        

        print("[INFO] Prediction encoding", self.math_util.calculate_prediction_encoding)

        darknet.add(
            layers.Dense(
                units=self.math_util.calculate_prediction_encoding(),
                activation = 'relu'
            )
        )

        print("[INFO] Completed")
        
        return darknet

    def create_input_layer(self):
        return layers.InputLayer(
            input_shape=(
                INPUT_CONFIG["image_width"], 
                INPUT_CONFIG["image_height"], 
                INPUT_CONFIG["image_channels"]
                )
            )

    def create_conv2d_layer(self, filters: int, kernel_size: int, strides: int) -> layers.Conv2D:
        return layers.Conv2D(
            filters,
            kernel_size=kernel_size,
            strides=strides,
            activation=self.math_util.leaky_relu(0.1),
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
