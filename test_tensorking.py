from tensorking import layers
from tensorking import models
from tensorking import activation
from tensorking import loss
from tensorking import debug

import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

model = models.Sequential(layers=[layers.Dense(1, activation=activation.Sigmoid), layers.Dense(1, activation=activation.Sigmoid)], loss=loss.MeanAbsoluteError)

X, y = spiral_data(samples=50, classes=3) 

transformed_y = np.reshape(y, (len(y), 1))

model.fit(X, transformed_y)