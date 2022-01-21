class Sequential:
    # List containing layer class'
    def __init__(self):
        self.layers = []


    def forward(self, inputs):
        
        for layer in self.layers:
            inputs = layer.forward(inputs)

        return inputs 

    # Fitting function
    def fit(self):
        pass