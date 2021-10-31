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

    '''
    iou (Intersection over Union) helper
    calculates
    '''
    def iou(self, box_pred, box_actual):
        
        # get edge coordinates by x/y_midpoint - x/y_width/2

        p_x1 = box_pred[:, :, :, :, 0:1] - box_pred[:, :, :, :, 2:3] / 2.0
        p_y1 = box_pred[:, :, :, :, 1:2] - box_pred[:, :, :, :, 3:4] / 2.0
        p_x2 = box_pred[:, :, :, :, 0:1] + box_pred[:, :, :, :, 2:3] / 2.0
        p_y2 = box_pred[:, :, :, :, 1:2] + box_pred[:, :, :, :, 3:4] / 2.0
        
        a_x1 = box_actual[:, :, :, :, 0:1] - box_actual[:, :, :, :, 2:3] / 2.0
        a_y1 = box_actual[:, :, :, :, 1:2] - box_actual[:, :, :, :, 3:4] / 2.0
        a_x2 = box_actual[:, :, :, :, 0:1] + box_actual[:, :, :, :, 2:3] / 2.0
        a_y2 = box_actual[:, :, :, :, 1:2] + box_actual[:, :, :, :, 3:4] / 2.0

        x_min_pred = tf.minimum(p_x1, p_x2)
        y_min_pred = tf.minimum(p_y1, p_y2)
        x_max_pred = tf.maximum(p_x1, p_x2)
        y_max_pred = tf.maximum(p_y1, p_y2)
        
        x_min_actual = tf.minimum(a_x1, a_x2)
        y_min_actual = tf.minimum(a_y1, a_y2)
        x_max_actual = tf.maximum(a_x1, a_x2)
        y_max_actual = tf.maximum(a_y1, a_y2)

        # Overlap in X direction
        x_over = tf.minimum(x_max_pred, x_max_actual) - tf.maximum(x_min_pred, x_min_actual)
        
        # Overlap in Y direction
        y_over = tf.minimum(y_max_pred, y_max_actual) - tf.maximum(y_min_pred, y_min_actual)
        
        # Area of overlap and boxes
        intersection_area = x_over * y_over

        # Area of total - intersection
        predicted_box_area = (x_max_pred - x_min_pred) * (y_max_pred - y_min_pred)
        actual_box_area = (x_max_actual - x_min_actual) * (y_max_actual - y_min_actual)

        union_area = tf.maximum(predicted_box_area + actual_box_area - intersection_area, 1e-6)

        return tf.clip_by_value(intersection_area / union_area, 0.0, 1.0)
 
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
