from tensorking import layers
from tensorking import models
from tensorking import activation
from tensorking import loss

import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

model = models.Sequential(layers=[layers.Dense(5), layers.Dense(1)], loss=loss.CategoricalCrossentropy)

X, y = spiral_data(samples=100, classes=3)

transformed_y = np.reshape(y, (len(y), 1))

model.fit(X, transformed_y)

