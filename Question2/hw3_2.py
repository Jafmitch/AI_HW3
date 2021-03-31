"""
- File: hw3_2.py
- Author: Jason A. F. Mitchell and Eric Tulowetzke
- Summary: This is the main module for homework 3 problem 2.
"""
import data_io as io
import graph_wrapper as gw
import math
import numpy as np
import policy as pie
import random as rand

COOLING_FACTOR = 0.9
INITIAL_TEMPERATURE = 3000
MAP_X = 50
MAP_Y = 50
MAX_ITERATIONS = 2000
NUMBER_OF_ACTIONS = 8
NUMBER_OF_TRIALS = 1000
PUNISHMENT_VALUE = -10
REWARD_VALUE = 10

# Macros for map array
OUT_OF_BOUNDS = -1
EMPTY = 0
START = 1
END = 2

# Macros for coordinates
X = 0
Y = 1


def main():
    """
    The main function of this module.
    """
    policyMap = np.array(initPolicyMap())
    mapArray, start, end = hardInit()
    # io.printMap(mapArray, [])
    for trial in range(NUMBER_OF_TRIALS):
        print(trial)
        policyMap, route = policyIterate(np.array(mapArray), start, end, policyMap)
    route = []
    policyMap, route = policyIterate(np.array(mapArray), start, end, policyMap)
    route.insert(0, start)
    io.printPolicyMap(policyMap)
    io.printMap(mapArray, route)


def accept_solution(energy1, energy2, temperature, current, new):
    """
    Function checks whether to accept or reject solution using an algorithm 
    similar to simulated annealing.

    Args:
        energy1 (float): fitness or energy of current solution
        energy2 (float): fitness or energy of new solution
        temperature (float): "temperature" value that determines probability of
                             accepting a better value
        current ([type]): [description]
        new ([type]): [description]

    Returns:
        [type]: [description]
    """
    if energy1 > energy2:
        return True, new[X], new[Y]
    else:
        try:
            a = math.exp((energy1 - energy2) / temperature)
        except ZeroDivisionError:
            a = 1
        b = rand.random()
        if a > b:
            return True, new[X], new[Y]
        else:
            return False, current[X], current[Y]


def distance(current_i, current_j, end_i, end_j):
    """
    Calculates distance of IJ values entered i from the endpoint
    :param current_i: X-coordinate
    :param current_j: Y-coordinate
    :param end_i: Ending point for the x-coordinate
    :param end_j: Ending point for the y-coordinate
    :return: Returns calculated distance
    """
    i = math.pow((end_i - current_i), 2)
    j = math.pow((end_j - current_j), 2)
    return math.sqrt((i + j))


def hardInit():
    """
    Initializes map array with a difficult out of bounds area.

    Returns:
        list: initialized 2d map array
        list: starting coordinates
        list: ending coordinates
    """
    mapArray = initMapArray()
    start = (rand.randint(0, 10), rand.randint(0, 49))
    end = (rand.randint(46, 49), rand.randint(0, 49))
    mapArray[start[X]][start[Y]] = START
    mapArray[end[X]][end[Y]] = END
    for i in range(rand.randint(12, 24), rand.randint(25, 44)):
        for j in range(rand.randint(12, 24), rand.randint(25, 44)):
            mapArray[i][j] = OUT_OF_BOUNDS
    return mapArray, start, end

def initMapArray():
    """
    Initialized map array by setting the size and filling all spaces with 0.

    Returns:
        list: initialized 2d map array
    """
    mapArray = []
    for x in range(MAP_X):
        rowArray = []
        for y in range(MAP_Y):
            rowArray.append(0)
        mapArray.append(rowArray)
    return mapArray


def initPolicyMap():
    policyMap = []
    for x in range(MAP_X):
        column = []
        for y in range(MAP_Y):
            item = []
            for actions in range(NUMBER_OF_ACTIONS):
                item.append(100)
            column.append(np.array(item))
        policyMap.append(column)
    return policyMap


def policyIterate(mapArray, start, end, policyMap):
    route = []
    i, j, iteration = start[X], start[Y], 0
    temperature = INITIAL_TEMPERATURE
    while (i != end[X] or j != end[Y]) and iteration < MAX_ITERATIONS:
        policy = pie.Policy(policyMap[i][j])
        new_i, new_j, action = policy.chooseNextState(i, j, policyMap, mapArray)
        accept, i, j = accept_solution(
            distance(i, j, end[X], end[Y]),
            distance(new_i, new_j, end[X], end[Y]),
            temperature,
            (i, j),
            (new_i, new_j)
        )
        temperature *= COOLING_FACTOR
        policyMap[new_i][new_j][action] = policyMap[new_i][new_j][action] + \
            (REWARD_VALUE if accept else PUNISHMENT_VALUE)
        iteration += 1
        # io.displayMap(mapArray, (i, j))
        route.append((i, j))
    return policyMap, route


def simpleInit():
    """
    Initializes map array with a simple out of bounds area.

    Returns:
        list: initialized 2d map array
        list: starting coordinates
        list: ending coordinates
    """
    mapArray = initMapArray()
    mapArray[5][25] = START
    mapArray[45][25] = END
    for i in range(15, 30):
        mapArray[i][i] = OUT_OF_BOUNDS
        mapArray[i][i + 1] = OUT_OF_BOUNDS
        mapArray[i + 1][i] = OUT_OF_BOUNDS
    return mapArray, [5, 25], [45, 25]


if __name__ == "__main__":
    main()
