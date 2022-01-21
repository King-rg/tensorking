import numpy as np

class Sequential():
    # List containing layer class'
    def __init__(self, layers: list, input_shape):
        self.layers = layers
        self.input_shape = input_shape

    def link(self):
        x=0
        while (x < len(self.layers)):
            self.layers[x]
            
            x=x+1

    def forward(self, inputs):
        output = 0

        for layer in self.layers:
            

        return output 

    # Fitting function
    def fit(self):
        pass