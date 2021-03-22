"""
- File: hw3.py
- Author: Jason A. F. Mitchell and Eric Tulowetzke
- Summary: This is the main module for homework 3 problem 1.
"""
import numpy as np
import data_io as io
import graph_wrapper as gw
import  neuron_layer as nl
import forward_propagation as fp
import backward_propagation as bp


def main():
    io.graphTrainingData()

    ##Three layer ANN
    ann = np.array([])
    for l in range(3):
        tmp = nl.NeuronLayer(2, 2)
        ann = np.append(ann, tmp)

    ##Separate the values into inputs(values) and known outcome values
    data_array = io.getTrainingData()
    len = int(data_array.shape[0])
    tmp = []
    values = []
    know = []
    for i in range(len):
        tmp = data_array[i][0:2]
        tmp = tmp.T
        values.append(tmp)
        tmp = data_array[i][2:4]
        tmp = tmp.T
        know.append(tmp)
    del tmp
    values = np.array(values)
    know = np.array(know)
    ##Feed in each input value into both forward propagation and back propagation
    loss = 1
    loss_arr = np.array([])
    for i in range(len):
        ann[0].input_value = values[i]
        loss_arr = np.append(loss_arr, fp.forward_network(ann, know[i])) #Collect the square difference of each pair
        test = bp.backprop(ann, know[i])

    loss = loss_arr.sum()/len #Finish calculating mean squared error
    print(loss)
    print(ann[0].dCdw)
    del loss_arr





if __name__ == "__main__":
    main()
