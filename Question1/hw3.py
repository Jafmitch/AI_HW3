"""
- File: hw3.py
- Author: Jason A. F. Mitchell and Eric Tulowetzke
- Summary: This is the main module for homework 3 problem 1.
"""
import backward_propagation as bp
import data_io as io
import forward_propagation as fp
import graph_wrapper as gw
import helper_functions as hf
import neuron_layer as nl
import numpy as np

BATCH = 240  # batch size
HIDDEM_DIM = 25
I_MAX = 100000
INPUT_DIM = 2
LEARNING_RATE = 5e-5
N_LAYER = 3  # number of Neuron layers
OUTPUT_DIM = 2
TRIALS = 10

def main():
    """
    The main function of this module.
    """
    io.graphTrainingData()
    io.graphTestingData()
    percentCorrectAnswers = []
    for trial in range(TRIALS):
        print(trial)
        ann = buildPerceptron(N_LAYER, INPUT_DIM, HIDDEM_DIM, OUTPUT_DIM)
        costs = trainANN(ann)
        temp = testANN(ann)
        percentCorrectAnswers.append(temp)
        io.graphCosts(costs, trial)
        io.graphActivationRegion(ann, trial)
    io.graphCorrectAnswers(percentCorrectAnswers)


def buildPerceptron(layers, i, h, o):
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
        if l == 0:
            tmp = nl.NeuronLayer(h, i)
        elif l == (layers - 1):
            tmp = nl.NeuronLayer(o, h)
        else:
            tmp = nl.NeuronLayer(h, h)
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
        if np.argmax([ann[N_LAYER - 1].a[0], ann[N_LAYER - 1].a[1]]) == \
           np.argmax([know[j][0], know[j][1]]):
            check += 1
    print("Number right", check)
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
    Returns:
        list: list of the cost of each iteration
    """
    costs = []

    # Feed in each input value into both forward propagation and back propagation
    values, know = getData()
    loss = 1
    k = 0
    while loss > 0.3 and k < I_MAX:
        loss_arr = np.array([])
        for i in range(BATCH):
            ann[0].input_value = values[i]
        # Collect the square difference of each pair
            sqdiff = fp.forward_network(ann, know[i])
            loss_arr = np.append(loss_arr, sqdiff)
            bp.backprop(ann, know[i])
        # Finish Average and the sum gradients and edit Weights
        for i in range(N_LAYER):
            ann[i].w -= ann[i].dCdw_sum/BATCH * LEARNING_RATE
            ann[i].zero_out()
        loss = loss_arr.sum() / BATCH
        costs.append(loss)
        if k % 1000 == 0:
            print(k, loss)
        k += 1
        del loss_arr
    return costs


if __name__ == "__main__":
    main()
