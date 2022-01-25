class model:
    def show_weights(model):
        try:
            for layer in model.layers:
                print(layer.weights.shape)
        except AttributeError:
            print('Make sure the layers are activated')