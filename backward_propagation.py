"""
- File: backward_propagation.py
- Author: Jason A. F. Mitchell
- Summary: This module is for calculating the backwards propagation of a
           neural network.
"""
import activation_functions as af
import helper_functions as hf
import neuron_layer as nl
import numpy as np

# derivative of the activation function used in the neural network
AF_PRIME = af.reluPrime


def backprop(nn, y):
    """
    Does backward propagation of a neural network. It accomplishes this by
    iterating backward through the neural network and calculates the partial
    derivatives of the Cost function relative to the weight of each layer.

    Args:
        nn (list): A list of NeuronLayer objects that represent layers of the
                   neural network.
        y (np.ndarray): Expected output values in a 1d array.

    Returns:
        np.ndarray: 1d array containing the gradient for each layer
    """
    LAST = len(nn) - 1

    # last layer
    nn[LAST].dCdz = hf.to2D(np.multiply(2.0 * (nn[LAST].a - y), AF_PRIME(nn[LAST].z)))
    nn[LAST].dCdw = np.dot(nn[LAST].dCdz.T, hf.to2D(nn[LAST].input_value))
    nn[LAST].dCdw_sum = np.add(nn[LAST].dCdw, nn[LAST].dCdw_sum)

    # other layers
    for n in range(1, len(nn)):
        dz1dz2 = \
            np.dot(nn[LAST - n + 1].w.T, nn[LAST - n + 1].dCdz.T)
        nn[LAST - n].dCdz = \
            np.multiply(hf.to2D(AF_PRIME(nn[LAST - n].z)), dz1dz2.T)
        nn[LAST - n].dCdw = \
            (np.dot(nn[LAST - n].dCdz.T, hf.to2D(nn[LAST - n].input_value)))
        nn[LAST - n].dCdw_sum = np.add(nn[LAST - n].dCdw, nn[LAST - n].dCdw_sum) #sum up Gradient weights as they are calculated

#temp for now
def backprop2(ann, know):
    layer = ann.shape[0] - 1
    ann[layer].gz = 2.0 * (ann[layer].a - know)
    ann[layer-1].ga = np.dot(ann[layer].w.T, ann[layer].gz)
    ann[layer - 1].gz = ann[layer-1].ga.copy()
    ann[layer - 1].gz = af.relu(ann[layer - 1].gz)
    ann[layer].gw = np.dot(ann[layer].gz, hf.T1D(ann[layer-1].ga))

    ann[layer - 2].ga = np.dot(ann[layer-1].w.T, ann[layer-1].gz)

    ann[layer-1].gw = np.dot(ann[layer - 1].gz, hf.T1D(ann[layer - 2].ga))
    ann[layer - 2].gz = ann[layer - 2].ga.copy()
    ann[layer - 2].gz = af.relu(ann[layer - 2].gz)
    ann[layer - 2].gw = np.dot(ann[layer - 2].gz, hf.T1D(ann[layer - 2].input_value))

    ann[layer - 2].dCdw_sum = np.add(ann[layer - 2].gw, ann[layer - 2].dCdw_sum)
    ann[layer-1].dCdw_sum = np.add(ann[layer - 1].gw, ann[layer - 1].dCdw_sum)
    ann[layer].dCdw_sum  = np.add(ann[layer].gw, ann[layer].dCdw_sum)