"""
- File: forward_propagation.py
- Author: Eric Tulowetzke
- Summary: This module contains a function for forward propagation of a artificial neural network
"""

import numpy as np
import activation_functions as a


def forward_network(neuron_layer_array, first=True):
    """
    This function accepts an numpy array of instances of the neuron layer class.
    Along with the number of layers that the ANN supposed to have.
    It then runs through forward propagation for all layers, and updates values in the layers.

    Args:
        neuron_layer_array: numpy array of neuron layer instances.

    Returns:
         neuron_layer_array[layer-1].a: is the last output layer of the ANN"""
    layer = int(neuron_layer_array.size)
    for l in range(0, layer):
        if first is True:
            input_value_t = neuron_layer_array[l].input_value.T
            neuron_layer_array[l].z = np.dot(neuron_layer_array[l].w, input_value_t)
            neuron_layer_array[l].a = a.relu(neuron_layer_array[l].z)
            first = False
        else:
            neuron_layer_array[l].z = np.dot(neuron_layer_array[l].w, neuron_layer_array[l-1].a)
            neuron_layer_array[l].a = a.relu(neuron_layer_array[l].z)
    return neuron_layer_array[layer-1].a

