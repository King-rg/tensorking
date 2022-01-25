import numpy as np

class CategoricalCrossentropy:
    def calculate(y_pred, y_true):
        loss = y_true*np.log(y_pred)
        return loss.mean()

class MeanSquareError:
    def calculate(y_pred, y_true):
        mse = (y_pred-y_true) ** 2
        return mse.mean()

class MeanAbsoluteError:
    def calculate(y_pred, y_true):
        mae = np.abs(y_pred-y_true) 
        return mae.mean()