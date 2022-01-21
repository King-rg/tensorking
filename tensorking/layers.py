import numpy as np

# Dense layer
class Dense:

    # Layer initialization
    def __init__(self, n_neurons):
        # Initialize weights and biases
        self.n_neurons = n_neurons
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        
        self.next_layer = False

    # Forward pass
    def forward(self, inputs):
        # Calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases

        if not False:
            return self.next_layer.forward(self.output)
        else:
            return self.output