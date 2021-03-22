"""
- File: backward_propagation.py
- Author: Jason A. F. Mitchell
- Summary: This module is for calculating the backwards propagation of a
           neural network.
"""
import activation_functions as af
import neuron_layer as nl
import numpy as np

# derivative of the activation function used in the neural network
AF_PRIME = af.reluPrime


def backprop(nn, y, x):
    """
    Does backward propagation of a neural network. It accomplishes this by
    iterating backward through the neural network and calculates the partial
    derivatives of the Cost function relative to the weight of each layer.

    Args:
        nn (list): A list of NeuronLayer objects that represent layers of the
                   neural network.
        y (ndarray): Expected output values
        x (ndarray): Input values

    Returns:
        ndarray: array containing gradient for each layer
    """
    LAST = len(nn) - 1
    gradients = []

    # last layer
    nn[LAST].dCdz = np.multiply(2.0 * (nn[LAST].a - y), AF_PRIME(nn[LAST].z))
    nn[LAST].dCdw = (np.dot(nn[LAST].dCdz, nn[LAST].input_value.T))
    gradients.append(nn[LAST].dCdw)

    # other layers
    for n in range(1, len(nn)):
        dz1dz2 = \
            np.dot(nn[LAST - n + 1].w.T, nn[LAST - n + 1].dCdz)
        nn[LAST - n].dCdz = \
            np.multiply(AF_PRIME(nn[LAST - n].z), dz1dz2)
        nn[LAST - n].dCdw = \
            (np.dot(nn[LAST - n].dCdz, nn[LAST - n].input_value.T))
        gradients.append(nn[LAST - n].dCdw)

    return np.array(gradients)
