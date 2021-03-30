"""
- File: hw3_2.py
- Author: Jason A. F. Mitchell and Eric Tulowetzke
- Summary: This is the main module for homework 3 problem 2.
"""
import numpy as np
import data_io as io
import graph_wrapper as gw

MAP_X = 50
MAP_Y = 50
MAX_ITERATIONS = 10000

# Macros for map array
OUT_OF_BOUNDS = -1
EMPTY = 0
START = 1
END = 2


def main():
    """
    The main function of this module.
    """
    mapArray, start, end = simpleInit()
    route = policyIterate(mapArray, start, end)
    io.printMap(mapArray, route)


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
    # init policy
    iteration = 0
    while (not exitCondition([5 + iteration + 1, 25 + (iteration % 2)], end)) and iteration < MAX_ITERATIONS:
        # copy policy into previous policy
        # compute V
        # choose new policy

        iteration += 1
        route.append([5 + iteration, 25 + (iteration % 2)])  # change later
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
        mapArray[i+1][i] = OUT_OF_BOUNDS
    return mapArray, [5, 25], [45, 25]


if __name__ == "__main__":
    main()
