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

COOLING_FACTOR = 0.1
INITIAL_TEMPERATURE = 3000
MAP_X = 50
MAP_Y = 50
MAX_ITERATIONS = 1000
NUMBER_OF_ACTIONS = 8
NUMBER_OF_TRIALS = 5000
PUNISHMENT_VALUE = -1
REWARD_VALUE = 1
X_ACTIONS = [-1, 1, 0, 0, -1, -1, 1, 1]
Y_ACTIONS = [0, 0, 1, -1, -1, 1, 1, -1]

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
    for trial in range(NUMBER_OF_TRIALS):
        print(trial)
        policyMap, route = policyIterate(
            np.array(mapArray), start, end, policyMap
        )
    route = []
    policyMap, route = policyIterate(np.array(mapArray), start, end, policyMap)
    io.printPolicyMap(policyMap)
    io.printMap(mapArray, route)


def acceptSolution(energy1, energy2, temperature):
    """
    Function checks whether to accept or reject solution using an algorithm
    similar to simulated annealing.

    Args:
        energy1 (float): fitness or energy of current solution
        energy2 (float): fitness or energy of new solution
        temperature (float): "temperature" value that determines probability of
                             accepting a better value

    Returns:
        bool: True if accept, false if not.
    """
    if energy1 > energy2:
        return True
    else:
        try:
            a = math.exp((energy1 - energy2) / temperature)
        except ZeroDivisionError:
            a = 1
        b = rand.random()
        if a > b:
            return True
        else:
            return False


def adjustWeights(policyMap, x, y, action, accept):
    """
    

    Args:
        policyMap (list): [description]
        x (int): [description]
        y (int): [description]
        action (int): [description]
        accept (bool): [description]

    Returns:
        [type]: [description]
    """
    for i in range(NUMBER_OF_ACTIONS):
        if i == action:
            policyMap[x][y][i] += (
                REWARD_VALUE if accept else PUNISHMENT_VALUE)
        policyMap[x][y][i] = 0 if policyMap[x][y][i] < 0 else policyMap[x][y][i]
        policyMap[x][y][i] = 1000 if policyMap[x][y][i] > 1000 else policyMap[x][y][i]
    return policyMap


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
    Initializes map array with a randomly generated out-of-bounds area.

    Returns:
        list: initialized 2d map array
        list: starting coordinates
        list: ending coordinates
    """
    mapArray = initMapArray()
    start = (rand.randint(0, int(MAP_X / 10)), rand.randint(0, MAP_Y - 1))
    end = (rand.randint(int(MAP_X - MAP_X / 10), MAP_Y - 1),
           rand.randint(0, MAP_Y - 1))
    mapArray[start[X]][start[Y]] = START
    mapArray[end[X]][end[Y]] = END

    upperX = int(MAP_X - MAP_X / 10 - 1)
    lowerX = int(MAP_X / 10 + 1)
    middleX = int(MAP_X / 2 - 1)
    upperY = MAP_Y - 2
    lowerY = 2
    middleY = int(MAP_Y / 2 - 1)
    for i in range(rand.randint(lowerX, middleX), rand.randint(middleX + 2, upperX)):
        for j in range(rand.randint(lowerY, middleY), rand.randint(middleY + 2, upperY)):
            mapArray[i][j] = OUT_OF_BOUNDS
    return mapArray, start, end


def hardishInit():
    """
    Creates an X-shape out-of-bounds area on the map.

    Returns:
        list: initialized 2d map array
        list: starting coordinates
        list: ending coordinates
    """
    mapArray = initMapArray()
    start = (int(MAP_X / 10), int(MAP_Y / 2))
    end = (int(MAP_X - MAP_X / 10), int(MAP_Y / 2))
    mapArray[start[X]][start[Y]] = START
    mapArray[end[X]][end[Y]] = END
    for i in range(int((3 * MAP_X) / 10), int((3 * MAP_X) / 5)):
        mapArray[int(MAP_X/2)+1][i] = OUT_OF_BOUNDS
        mapArray[int(MAP_X/2)][i] = OUT_OF_BOUNDS
        mapArray[MAP_X - i][i] = OUT_OF_BOUNDS
        mapArray[MAP_X - i][i+1] = OUT_OF_BOUNDS
        mapArray[i][i] = OUT_OF_BOUNDS
        mapArray[i][i + 1] = OUT_OF_BOUNDS
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
    """
    Initializes the policy map by setting all weights to 0 at each square.

    Returns:
        list: 3d list of policy weights.
    """
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
    """
    Iterate weights in the policy to create the best policy map.

    Args:
        mapArray (list): List structure representing the playing field of the
                         problem.
        start (tuple): Starting coordinates.
        end (tuple): End coordinates.
        policyMap (list): 3d list record of policy weight values.

    Returns:
        list: Updated policy map.
        list: Route taken over the course of the problem.
    """
    route = [start]
    i, j, iteration = start[X], start[Y], 0
    temperature = INITIAL_TEMPERATURE
    while (i != end[X] or j != end[Y]) and iteration < MAX_ITERATIONS:
        policy = pie.Policy(policyMap[i][j])
        new_i, new_j, action = policy.chooseNextState(
            i, j, policyMap, mapArray)
        accept = acceptSolution(
            distance(i, j, end[X], end[Y]),
            distance(new_i, new_j, end[X], end[Y]),
            temperature
        )
        temperature *= COOLING_FACTOR
        policyMap = adjustWeights(policyMap, i, j, action, accept)
        i = new_i
        j = new_j
        iteration += 1
        # io.displayMap(mapArray, (i, j))
        route.append((i, j))
    return policyMap, route


def simpleInit():
    """
    Initializes map array with a simple out-of-bounds area.

    Returns:
        list: initialized 2d map array
        list: starting coordinates
        list: ending coordinates
    """
    mapArray = initMapArray()
    start = (int(MAP_X / 10), int(MAP_Y / 2))
    end = (int(MAP_X - MAP_X / 10), int(MAP_Y / 2))
    mapArray[start[X]][start[Y]] = START
    mapArray[end[X]][end[Y]] = END
    for i in range(int((3 * MAP_X)/10), int((3 * MAP_X)/5)):
        mapArray[i][i] = OUT_OF_BOUNDS
        mapArray[i][i + 1] = OUT_OF_BOUNDS
        mapArray[i + 1][i] = OUT_OF_BOUNDS
    return mapArray, start, end


if __name__ == "__main__":
    main()
