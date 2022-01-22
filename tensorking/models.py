import numpy as np

class Sequential():
    """
    1. Get input data
    2. Check number of inputs
    3. Begin network preparation
    4. Run layer activation
    """
    
    # List containing layer class'
    def __init__(self, layers: list):
        self.layers = layers

    def prepare(self, inputs):
        x=0
        while (x < len(self.layers)):
            if (x == 0):
                self.layers[x].activate(inputs.shape[len(inputs.shape)-1])
                if (x < len(self.layers)-1):
                    self.layers[x].next_layer = self.layers[x+1]
            else:
                self.layers[x].activate(self.layers[x-1].n_neurons)
                if (x < len(self.layers)-1):
                        self.layers[x].next_layer = self.layers[x+1]
            x=x+1

    def forward(self, inputs):
        self.prepare(inputs)
        
        return self.layers[0].forward(inputs)

    # Fitting function
    def fit(self):
        pass