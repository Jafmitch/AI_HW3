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

OUT_OF_BOUNDS = -1
EMPTY = 0
CURRENT = 1
END = 2


def main():
    """
    The main function of this module.
    """
    mapArray = simpleInit()
    io.printMap(mapArray)


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


def simpleInit():
    """
    Initializes map array with a simple out of bounds area.

    Returns:
        list: initialized 2d map array
    """
    mapArray = initMapArray()
    mapArray[5][25] = CURRENT
    mapArray[45][25] = END
    for i in range(15, 30):
        mapArray[i][i] = OUT_OF_BOUNDS
    return mapArray


if __name__ == "__main__":
    main()
