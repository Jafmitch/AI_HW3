"""
- File: policy.py
- Author: Eric Tulowetzke
- Summary: 
"""
import numpy as np
import random as rand

NUMBER_OF_ACTIONS = 8

# Macros for map array
OUT_OF_BOUNDS = -1
EMPTY = 0
START = 1
END = 2

# Macros for direction
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
DOWN_LEFT = 4
UP_LEFT = 5
UP_RIGHT = 6
DOWN_RIGHT = 7


def valid(i, j, map_array):
    """
    Static class function, designed to determine if a new position is valid
    Args:
        i(int): x-coordinate
        j(int): y-coordinate
        map_array(numpy array 2D): Map of current field

    Return:
        True if valid position to move to
    """
    rows = map_array.shape[0]
    cols = map_array.shape[1]
    if i < 0 or i >= rows:
        return False
    if j < 0 or j >= cols:
        return False
    if map_array[i, j] == OUT_OF_BOUNDS:
        return False
    return True


class Policy:
    """
    Policy class A current state is entered into the class with the map,
     then an action is made and updated map is returned. Probabilities of actions can vary over time.
    """

    def __init__(self, weights):
        self.weights = np.array(weights)
        for weight in self.weights:
            weight = 0 if weight < 0 else weight

    def chooseNextState(self, x, y, policyMap, mapArray):
        new_x, new_y, action = self.__getNewState(x, y)
        while not valid(new_x, new_y, mapArray):
            self.weights = self.weights + 1
            self.weights[action] = 0
            new_x, new_y, action = self.__getNewState(x, y)
        return new_x, new_y, action

    def __getNewState(self, x, y):
        sumOfAll = self.__sumTotal(NUMBER_OF_ACTIONS)
        if sumOfAll <= 0:
            self.weights = self.weights + 1
            sumOfAll = NUMBER_OF_ACTIONS
        randomNumber = rand.randrange(sumOfAll)
        if randomNumber < self.__sumTotal(1):
            return x - 1, y, LEFT
        elif randomNumber < self.__sumTotal(2):
            return x + 1, y, RIGHT
        elif randomNumber < self.__sumTotal(3):
            return x, y + 1, UP
        elif randomNumber < self.__sumTotal(4):
            return x, y - 1, DOWN
        elif randomNumber < self.__sumTotal(5):
            return x - 1, y - 1, DOWN_LEFT
        elif randomNumber < self.__sumTotal(6):
            return x - 1, y + 1, UP_LEFT
        elif randomNumber < self.__sumTotal(7):
            return x + 1, y + 1, UP_RIGHT
        elif randomNumber < self.__sumTotal(8):
            return x + 1, y - 1, DOWN_RIGHT
        else:
            return x, y, -1

    def __sumTotal(self, numberOfElements):
        sumTotal = 0
        for n in range(numberOfElements):
            sumTotal += self.weights[n]
        return sumTotal
