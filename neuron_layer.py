import numpy as np

class NeuronLayer:
    def __init__(self, input_dim, output_dim):
        self.input_value = np.array([])
        self.w = np.random.rand(input_dim, output_dim)
        self.z = np.array([])
        self.a = np.array([])
        self.grad_weight = np.array([])
        self.grad_z = np.array([])
        self.grad_a = np.array([])
