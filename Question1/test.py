import numpy as np
import neuron_layer as nl
import forward_propagation as fp
import backward_propagation as bp
import helper_functions as hf


def test():
    x = hf.T1D(np.array([3, 2]))
    y = hf.T1D(np.array([10, 3]))
    perceptron = np.array([])
    for l in range(2):
        if l == 0:
            tmp = nl.NeuronLayer(2, 2)
        elif l == (2 - 1):
            tmp = nl.NeuronLayer(2, 2)
        else:
            tmp = nl.NeuronLayer(2, 2)
        perceptron = np.append(perceptron, tmp)

    perceptron[0].input_value = x
    perceptron[0].w = np.matrix('1 -2; -2 3', dtype=float)
    perceptron[1].w = np.matrix('4 1; 3 -1', dtype=float)

    fp.forward_network(perceptron, y)
    print("forward_network:")
    for l in range(2):
        print("layer", l)
        print("x", perceptron[l].input_value)
        print("W", perceptron[l].w)
        print("z", perceptron[l].z)
        print("a", perceptron[l].a)
        print("dz", perceptron[l].dCdz)
        print("dw", perceptron[l].dCdw)
    bp.backprop(perceptron, y)
    print("backprop:")
    for l in range(2):
        print("layer", l)
        print("x", perceptron[l].input_value)
        print("W", perceptron[l].w)
        print("z", perceptron[l].z)
        print("a", perceptron[l].a)
        print("dz", perceptron[l].dCdz)
        print("dw", perceptron[l].dCdw)

test()