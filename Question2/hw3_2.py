"""
- File: hw3_2.py
- Author: Jason A. F. Mitchell and Eric Tulowetzke
- Summary: This is the main module for homework 3 problem 2.
"""
import numpy as np
import data_io as io
import graph_wrapper as gw
import policy as pie
import math
import random as ran

MAP_X = 50
MAP_Y = 50
MAX_ITERATIONS = 10000
TEMP = 3000
COOLING = 0.999

# Macros for map array
OUT_OF_BOUNDS = -1
EMPTY = 0
START = 1
CURRENT = 2
END = 3


def main():
    """
    The main function of this module.
    """
    mapArray, start, end = simpleInit()
    route = policyIterate(mapArray, start, end)
    io.printMap(mapArray, route)


def accept_solution(energy1, energy2, temperature, oi, oj, ni, nj):
    """
    Simulating annealing function
    :param energy1: The old distance
    :param energy2: The new distance
    :param temperature: Current temperature
    :param oi: Old X
    :param oj: Old y
    :param ni: New x
    :param nj: new y
    :return: Returns rather the action is good or bad and what appropriate X and Y values need to be returned
    """
    if energy1 > energy2:
        return True, ni, nj
    else:
        a = math.exp((energy1 - energy2) / temperature)
        b = ran.random()
        if a > b:
            return True, ni, nj
        else:
            return False, oi, oj


def dist(current_i, current_j, end_i, end_j):
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


def exitCondition(start, end):
    X = 0
    Y = 1
    # replace later
    return start[X] == end[X]


def initMapArray():
    """
    Initialized map array by setting the size and filling all spaces with 0.

    Returns:
        list: initialized 2d map array
    """
    mapArray = []
    for y in range(MAP_Y):
        rowArray = []
        for x in range(MAP_X):
            rowArray.append(0)
        mapArray.append(rowArray)
    return mapArray


def policyIterate(mapArray, start, end):
    # NOTE: this is just a temporary filler until policy class gets written

    route = [start]
    p = pie.Policy()
    map_array = np.array(mapArray)
    # Initialize beginning x and Y coordinates
    i, j, k = 5, 25, 0
    t = TEMP
    while i != 45 or j != 25:
        new_i, new_j, map_array = p.new_policy(i=i, j=j, map_array=map_array)
        old_dist = dist(current_i=i, current_j=j, end_i=45, end_j=25)
        new_dist = dist(current_i=new_i, current_j=new_j, end_i=45, end_j=25)
        outcome, i, j = accept_solution(
            old_dist, new_dist, t, i, j, new_i, new_j)
        t *= COOLING
        p.update_policy(outcome=outcome)
        k += 1
    print(k)
    return route


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
