import numpy as np

class ReLU():
    # Forward pass
    def forward(inputs):
        # Calculate output values from inputs
        return np.maximum(0, inputs)




# Softmax activation
class Softmax:
    # Forward pass
    def forward(inputs):

        # Get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1,
                                            keepdims=True))
        # Normalize them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1,
                                            keepdims=True)

        return probabilities

class Sigmoid:
    def forward(inputs):

        exponentiate = 1 + np.exp(-inputs)

        sigmoid = 1 / exponentiate

        return sigmoid
