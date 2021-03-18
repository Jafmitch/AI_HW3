import numpy as np
from time import process_time_ns
from dataclasses import dataclass, field


@dataclass
class neuron:
    input: np.ndarray = field(init=False,
                              default_factory=lambda: np.array([],
                                                               dtype=float).T)
    weight: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=float))
    output: np.ndarray = field(init=False,
                               default_factory=lambda: np.array([],
                                                                dtype=float))


class FeedForwardNetwork_Vectorised:

    def __init__(self, d_in, d_hidden, layer):
        np.random.seed(process_time_ns())
        self.d_in = d_in
        self.d_hidden = d_hidden
        self.layer = layer
        self.tmp_layer = self.layer

    def ReLU(self, X):
        return np.maximum(X, 0)

    def forward_pass(self, neuron, input, odd=True, first=True):
        if self.layer != 0 and first is True:
            weight = np.random.randn(self.d_in, self.d_hidden)
            neuron.weight = np.append(neuron, weight)
            z = np.dot(weight, neuron.input)
            a = self.ReLU(z)
            self.layer -= 1
            return self.forward_pass(neuron, a, False, False)
        elif self.layer != 0 and odd is True:
            weight = np.random.randn(self.d_in, self.d_hidden)
            neuron.weight = np.append(neuron, weight)
            z = np.dot(weight, input)
            a = self.ReLU(z)
            self.layer -= 1
            return self.forward_pass(neuron, a, False, False)
        elif self.layer != 0 and odd is False:
            weight = np.random.randn(self.d_hidden, self.d_in)
            neuron.weight = np.append(neuron, weight)
            z = np.dot(weight, input)
            a = self.ReLU(z)
            self.layer -= 1
            return self.forward_pass(neuron, a, True, False)
        else:
            return input
