
import numpy as np

# Dense layer
class Dense:

    # Layer initialization
    def __init__(self, n_neurons, activation = False):
        # Initialize weights and biases
        self.n_neurons = n_neurons
        self.biases = np.zeros((1, n_neurons))
        self.activation = activation

        self.next_layer = False
 
    # Create the weights necessary for the forward function
    def activate(self, n_inputs):
        self.weights = 0.01 * np.random.randn(n_inputs,self.n_neurons)

    # Forward pass
    def forward(self, inputs):
        # Calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases

        # Apply activation function if needed
        if self.activation != False:
            self.output = self.activation.forward(self.output)

        if self.next_layer != False:
            return self.next_layer.forward(self.output)
        else:
            return self.output