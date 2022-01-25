import numpy as np

# Common loss class
class CategoricalCrossentropy:
    def calculate(y_pred, y_true):
        print(y_pred)
        loss = y_true*np.log(y_pred)
        return loss

class MeanSquareError:
    def calculate(y_pred, y_true):
        pass