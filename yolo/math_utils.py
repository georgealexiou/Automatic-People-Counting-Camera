from tensorflow.keras.backend import maximum

class MathUtil:
    def leaky_relu(self, alpha):
        return lambda val : maximum(alpha * val, val)