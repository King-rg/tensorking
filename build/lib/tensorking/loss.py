import numpy as np

# Common loss class
class CategoricalCrossentropy:
    def calculate(y_pred, y_true):
        loss = y_pred*np.log(y_true)
        return loss.mean()

class MeanSquareError:
    def calculate(y_pred, y_true):
        pass