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
import helper_functions as hf

BATCH = 100 # batch size
N_LAYER = 3 #number of Nneuron layers
LEARNING_RATE = 1e-5

def main():
    io.graphTrainingData()

    ##Three layer ANN
    ann = np.array([])
    for l in range(N_LAYER):
        tmp = nl.NeuronLayer(2, 2)
        ann = np.append(ann, tmp)

    
    ##Feed in each input value into both forward propagation and back propagation
    loss = 1
    k = 0
    values, know = shuffle_data()
    while loss > 0.01:
        grand_arr = []
        loss_arr = np.array([])
        for i in range(BATCH):
            ann[0].input_value = values[i]
            loss_arr = np.append(loss_arr, fp.forward_network(ann, know[i])) #Collect the square difference of each pair
            bp.backprop2(ann, know[i])

        #Finish Average and the sum gradients and edit Weights
        for i in range(N_LAYER):
            ann[i].w -= (ann[i].dCdw_sum * 1/BATCH) * LEARNING_RATE
            ann[i].zero_out()

        loss = loss_arr.sum()/BATCH #Finish calculating mean squared error
        if k %1000 == 0:
            print(k, loss)
        k += 1
        del loss_arr
        del grand_arr


def shuffle_data():
    """
        This function accepts Randomizes  the training dataset, so that we can get a large range of data values.
         It returns input values and known values with the transpose already taken of the respective values

        Returns:
             Returns numpy arrays of input and know output"""
    ##Separate the values into inputs(values) and known outcome values
    data_array = io.getTrainingData()
    np.random.shuffle(data_array)
    layer = int(data_array.shape[0])
    values = []
    know = []
    for i in range(layer):
        tmp = hf.T1D(data_array[i][0:2])
        values.append(tmp)
        del tmp
        tmp = hf.T1D(data_array[i][2:4])
        know.append(tmp)
        del tmp
    values = np.array(values)
    know = np.array(know)
    return values, know





if __name__ == "__main__":
    main()
