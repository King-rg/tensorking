import numpy as np

class Sequential():
    """
    1. Get input data
    2. Check number of inputs
    3. Begin network preparation
    4. Run layer activation
    """
    
    # List containing layer class'
    def __init__(self, layers: list, loss = False):
        self.layers = layers
        self.loss = loss

    # This function prepares the layers on the network to be stacked on each other.
    def prepare(self, inputs):
        
        def link(x):
            if (x < len(self.layers)-1):
                    self.layers[x].next_layer = self.layers[x+1]

        x=0
        while (x < len(self.layers)):
            if (x == 0):
                self.layers[x].activate(inputs.shape[len(inputs.shape)-1])
                link(x)
            else:
                self.layers[x].activate(self.layers[x-1].n_neurons)
                link(x)
            x=x+1

    # This propogates inputs through the network
    def forward(self, inputs):
        self.prepare(inputs) 
        return self.layers[0].forward(inputs)

    # Fitting function
    def fit(self, x, y, epochs=5, lr=0.0001):
        if self.loss == False:
            print('ERROR: No loss function provided')
        else:
            
            epoch=0
            while (epoch < epochs): 
                output = self.forward(x)
                if (np.array_equiv(output,y)):
                    loss = self.loss.calculate(output, y)
                    
                    print(loss)

                    self.layers[0].weights[0][0] = self.layers[0].weights[0][0]-lr

                    epoch=epoch+1
                else:
                    print(output.shape)
                    print(y.shape)
                    print('ERROR: Please ensure the output is the same shape as the Y variable')
                    return -1
