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
    #io.graphTrainingData()

    ##Three layer ANN
    ann = np.array([])
    for l in range(N_LAYER):
        tmp = nl.NeuronLayer(2, 2)
        ann = np.append(ann, tmp)

    
    ##Feed in each input value into both forward propagation and back propagation
    p_loss = 2
    loss = 1
    k = 0
    values, know = data()
    while p_loss > loss:
        p_loss = loss
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
    test_ann(ann)


def data(train=True):
    """
        This function accepts Randomizes the training dataset, so that we can get a large range of data values.
         It returns input values and known values with the transpose already taken of the respective values
         It will also retrieve the testing data values.

         Args:
             train(bool): Returns train data info if true

        Returns:
             Returns numpy arrays of input and know output"""
    ##Separate the values into inputs(values) and known outcome values
    if train:
        data_array = io.getTrainingData()
        np.random.shuffle(data_array)
        num_data = BATCH
    else:
        data_array = io.getData()
        num_data = int(data_array.shape[0])
    values = []
    know = []
    for i in range(num_data):
        tmp = hf.T1D(data_array[i][0:2])
        values.append(tmp)
        del tmp
        tmp = hf.T1D(data_array[i][2:4])
        know.append(tmp)
        del tmp
    values = np.array(values)
    know = np.array(know)
    return values, know


def test_ann(ann):
    """
        This function Where tests how good the artificial no network is compared to the testing data.
         It will print the percentage of correct answers.

             Args:
                 ann(array of Neuron layer class):
    """
    values, know = data(False)
    layer = values.shape[0]
    check = 0
    for j in range(layer):
        ann[0].input_value = values[j]
        fp.forward_network(ann, know[j])
        test = np.around(know[j])
        guess = np.around(ann[N_LAYER - 1].a)
        comp = guess == test
        if comp.all():
            check += 1
    print("Number right", check)
    print("Total data points", layer)
    print("testpercentage ", check/layer)

if __name__ == "__main__":
    main()
