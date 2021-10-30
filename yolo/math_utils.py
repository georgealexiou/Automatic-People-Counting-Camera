from tensorflow.keras.backend import maximum
import numpy as np
from configs.arch import INPUT_CONFIG


class MathUtil:

    def calculate_prediction_encoding(self):
        s_sqr = (INPUT_CONFIG["S_grid"] * INPUT_CONFIG["S_grid"])
        box_x5 = (INPUT_CONFIG["B_predictions"] * 5)
        c_classes = INPUT_CONFIG["C_classes"]
        return s_sqr * (box_x5 + c_classes)


    def leaky_relu(self, alpha):
        return lambda val: maximum(alpha * val, val)

    def relu(self):
        return lambda val: maximum(0, val)

    def heaviside_step(self):
        return lambda val: 1 if val > 0 else 0

    def sigmoid_linear_unit(self):
        return lambda val: val / ((np.e ** - val) + 1)

    def exponential_linear_unit(self, alpha):
        return lambda val: val if val > 0 else alpha * ((np.e ** val) - 1)

    def hypobolic_tangent(self):
        return lambda val: np.tanh(val)

    def identity(self):
        return lambda val: val

    def sigmoid(self):
        return lambda val: 1 / ((np.e ** - val) + 1)

    def mish(self):
        return lambda val: val * np.tanh(np.log((np.e ** val) - 1))
