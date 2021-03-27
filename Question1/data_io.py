
"""
- File: data_io.py
- Author: Jason A. F. Mitchell
- Summary: This module is for imputing and outputing files. This includes 
           things like importing data and converting it to an array as well 
           as outputing figures based on data used in the overall program.
"""

import graph_wrapper as gw
import neuron_layer as nl
import numpy as np

DATA_FILE = "datafiles/testdata.dat"
TRAINING_DATA_FILE = "datafiles/datafile.dat"
COLORS = ["b", "r", "g", "c", "m", "y", "orange", "purple", "lime", "pink"]


def getData(fileName=DATA_FILE):
    """
    This function reads data from a file and converts it to a 2d array of 
    floats. It expects the file to be a list with commas seperating items and
    new lines seperating rows.
    Example: 
    <item_1>, <item_2>, <item_3>
    <item_4>, <item_5>, <item_6>
    etc.

    Args:
        fileName (str, optional): Name of file to read. Defaults to DATA_FILE.

    Returns:
        ndarray: 2d array of the file's contents
    """
    CATEGORY = 2
    dataArray = []
    with open(fileName) as f:
        for line in f.read().split("\n"):
            temp = []
            if line != '':
                for item in line.split(","):
                    temp.append(float(item.strip()))
                if temp[CATEGORY] == 1.0:
                    temp[2:3] = [0, 1]
                else:
                    temp[2:3] = [1, 0]
                dataArray.append(temp)
    return np.array(dataArray)


def getTrainingData():
    """
    This function reads data specifically from the training data file specified
    in TRAINING_DATA_FILE.

    Returns:
        ndarray: 2d array of the file's contents
    """
    return getData(TRAINING_DATA_FILE)


def graphCorrectAnswers(percentCorrectAnswers):
    """
    Creates a graph of the percent correct answers per trial.

    Args:
        percentCorrectAnswers (list): list of percentCorrectAnswers per trial.
    """
    plot = gw.Plot()
    for i in range(len(percentCorrectAnswers)):
        plot.addPoint(i, percentCorrectAnswers[i], "o", "purple")

    plot.label("Percent Answers Correct per Trial",
               "Trial", "Percent of Answers Correct ")
    plot.save("correct_answers.jpg")
    plot.freeze()


def graphCosts(costs, number=0):
    """
    Creates a graph of the cost function results per iteration.

    Args:
        costs (list): List of cost function results per iteration.
        number (int): Number assigned to graph when doing multiple
                      trials. Default is 0.
    """
    plot = gw.Plot()
    plot.pointplot(range(len(costs)), costs, "blue")

    plot.label("Cost per Iteration",
               "Iteration Number", "Cost")
    plot.save("cost_per_iteration_trial" + str(number) +".jpg")
    plot.freeze()


def graphTestingData():
    """
    Uses graph wrapper to graph datafile data.
    """
    X = 0
    Y = 1
    CATEGORY = 2

    plot = gw.Plot()
    for row in getData(DATA_FILE):
        if row[CATEGORY] == 1:
            plot.addPoint(row[X], row[Y], "o", "blue")
        else:
            plot.addPoint(row[X], row[Y], "o", "red")

    plot.label("Data Set",  "x", "y")
    plot.save("data_set.jpg")
    plot.freeze()


def graphTrainingData():
    """
    Uses graph wrapper to graph training data.
    """
    X = 0
    Y = 1
    CATEGORY = 2

    plot = gw.Plot()
    for row in getTrainingData():
        if row[CATEGORY] == 1:
            plot.addPoint(row[X], row[Y], "o", "blue")
        else:
            plot.addPoint(row[X], row[Y], "o", "red")

    plot.label("Training Data",  "x", "y")
    plot.save("training_data.jpg")
    plot.freeze()
