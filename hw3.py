"""
- File: hw3.py
- Author: Jason A. F. Mitchell and Eric Tulowetzke
- Summary: This is the main module for homework 3 problem 1.
"""
import numpy as np
import data_io as io
import graph_wrapper as gw
import neuron_layer as nl
import forward_propagation as fp
import backward_propagation as bp
import helper_functions as hf

BATCH = 100  # batch size
N_LAYER = 3  # number of Neuron layers
LEARNING_RATE = 1e-5
TRIALS = 20


def main():
    """
    The main function of this module.
    """
    # io.graphTrainingData()
    percCorrectAnswers = []
    for trial in range(TRIALS):
        print(trial)
        ann = buildPerceptron(N_LAYER, 2, 2)
        trainANN(ann)
        temp = testANN(ann)
        percCorrectAnswers.append(temp)
    io.graphCorrectAnswers(percCorrectAnswers)

def buildPerceptron(layers, n, m):
    """
    This function creates an artificial neural network multi-layer perceptron
    using the NeuronLayer object.

    Args:
        layers (int): number of layers in the perceptron
        n ([type]): n dimension of the perceptron
        m ([type]): m dimension of the perceptron

    Returns:
        np.ndarray: array of NeuronLayers representing the perceptron
    """
    perceptron = np.array([])
    for l in range(layers):
        tmp = nl.NeuronLayer(n, m)
        perceptron = np.append(perceptron, tmp)
    return perceptron

def getData(train=True):
    """
        This function randomizes the training dataset, so that it can get a large range of data values.
        It returns input values and known values with the transpose already taken of the respective values
        It will also retrieve the testing data values.

        Args:
            train(bool): Returns train data info if true

        Returns:
            Returns numpy arrays of input and know output
    """
    # Separate the values into inputs(values) and known outcome values
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


def testANN(ann):
    """
        This function tests how good the artificial neural network is compared to the testing data.
        It will print the percentage of correct answers.

        Args:
            ann(array of Neuron layer class):
        Returns:
            float: number of correct values calculated by the ANN
    """
    values, know = getData(False)
    layer = values.shape[0]
    check = 0
    for j in range(layer):
        ann[0].input_value = values[j]
        fp.forward_network(ann, know[j])
        # test = np.around(know[j])
        # guess = np.around(ann[N_LAYER - 1].a)
        # comp = guess == test
        # if comp.all():
        #     check += 1
        if (ann[N_LAYER - 1].a[0] > ann[N_LAYER - 1].a[1]) == (know[j][0] < know[j][1]):
            check += 1
    # print("Number right", check)
    # print("Total data points", layer)
    # print("testpercentage ", check / layer)
    return check / layer
    
def trainANN(ann):
    """
    This function trains the neural network by feeding it training data and
    adjusting its weights according to a calculated gradient.

    Args:
        ann (np.ndarray): An artificial neural network represented by an array
                          or NeuronLayer objects
    """
    # Feed in each input value into both forward propagation and back propagation
    p_loss = 2
    loss = 1
    k = 0
    values, know = getData()
    while p_loss > loss:
        p_loss = loss
        grand_arr = []
        loss_arr = np.array([])
        for i in range(BATCH):
            ann[0].input_value = values[i]
            # Collect the square difference of each pair
            squareDifference = fp.forward_network(ann, know[i])
            loss_arr = np.append(loss_arr, squareDifference)
            bp.backprop(ann, know[i])
            # print("-------")
            # print(ann[len(ann) - 1].a[0], " | ", know[i][0])
            # print(ann[len(ann) - 1].a[1], " | ", know[i][1])
            # print("-------")

        # Finish Average and the sum gradients and edit Weights
        for i in range(N_LAYER):
            ann[i].w -= (ann[i].dCdw_sum * 1/BATCH) * LEARNING_RATE
            ann[i].zero_out()

        loss = loss_arr.sum()/BATCH  # Finish calculating mean squared error
        # if k % 1000 == 0:
        #     print(k, loss)
        k += 1
        del loss_arr
        del grand_arr


if __name__ == "__main__":
    main()
