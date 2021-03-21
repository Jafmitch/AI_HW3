import numpy as np
import neuron_layer as n


class ForwardNetwork:

    def __init__(self, layer):
        self.layer = int(layer)

    def relu(self, x_array):
        return np.maximum(x_array, 0)

    def forward_pass(self, neuron_layer_array, first=True):
        for l in range(0, self.layer):
            if first is True:
                input_value_t = neuron_layer_array[l].input_value.T
                neuron_layer_array[l].z = np.dot(neuron_layer_array[l].w, input_value_t)
                neuron_layer_array[l].a = self.relu(neuron_layer_array[l].z)
                first = False
            else:
                neuron_layer_array[l].z = np.dot(neuron_layer_array[l].w, neuron_layer_array[l-1].a)
                neuron_layer_array[l].a = self.relu(neuron_layer_array[l].z)
        return neuron_layer_array[self.layer-1].a




def main():
    ann = np.array([])
    for l in range(3):
        tmp = n.NeuronLayer(2, 2)
        ann = np.append(ann, tmp)

    values = np.array([1, 2])
    ann[0].input_value = np.append(ann[0].input_value, values)
    forward = ForwardNetwork(3)
    end = forward.forward_pass(ann)
    for l in range(3):
        print("layer ", l)
        print("input")
        print(ann[l].input_value)
        print("w")
        print(ann[l].w)
        print("z")
        print(ann[l].z)
        print("a")
        print(ann[l].a)

    print("end, ", end)


if __name__ == '__main__':
    main()

