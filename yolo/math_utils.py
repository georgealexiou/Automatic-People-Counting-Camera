import tensorflow as tf
import numpy as np
from configs.arch import INPUT_CONFIG


class MathUtil:

    # Model Helpers

    def calculate_prediction_encoding(self):
        s_sqr = (INPUT_CONFIG["S_grid"] * INPUT_CONFIG["S_grid"])
        box_x5 = (INPUT_CONFIG["B_predictions"] * 5)
        c_classes = INPUT_CONFIG["C_classes"]
        return s_sqr * (box_x5 + c_classes)

    # Loss Function Helpers

    def iou(self, box_pred, box_actual):
        
        p_x1 = box_pred[:, :, :, :, 0:1] - box_pred[:, :, :, :, 2:3] / 2.0
        p_y1 = box_pred[:, :, :, :, 1:2] - box_pred[:, :, :, :, 3:4] / 2.0
        p_x2 = box_pred[:, :, :, :, 0:1] + box_pred[:, :, :, :, 2:3] / 2.0
        p_y2 = box_pred[:, :, :, :, 1:2] + box_pred[:, :, :, :, 3:4] / 2.0
        
        a_x1 = box_actual[:, :, :, :, 0:1] - box_actual[:, :, :, :, 2:3] / 2.0
        a_y1 = box_actual[:, :, :, :, 1:2] - box_actual[:, :, :, :, 3:4] / 2.0
        a_x2 = box_actual[:, :, :, :, 0:1] + box_actual[:, :, :, :, 2:3] / 2.0
        a_y2 = box_actual[:, :, :, :, 1:2] + box_actual[:, :, :, :, 3:4] / 2.0

        # box1 = tf.stack(a_x1, a_y1, a_x2, a_x2)

        x1 = tf.maximum(p_x1, a_x1)
        y1 = tf.maximum(p_y1, a_y1)
        x2 = tf.minimum(p_x2, a_x2)
        y2 = tf.minimum(p_y2, a_y2)

        # Overlap in X direction
        x_over = x2-x1

        # Overlap in Y direction

        # Area of overlap

        # Area of total - intersection

        inter_box = tf.maximum(0.0, right_down - left_up)

        return None



    # Activation Functions

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
