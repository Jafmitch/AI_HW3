"""
- File: policy.py
- Author: Jason Mitchell and Eric Tulowetzke
- Summary: This module contains the Policy class and helper functions associated
           with said class. It also contains a PolicyException class for user
           generated exceptions.
"""
import numpy as np
import random as rand

NUMBER_OF_ACTIONS = 8
X_ACTIONS = [-1, 1, 0, 0, -1, -1, 1, 1]
Y_ACTIONS = [0, 0, 1, -1, -1, 1, 1, -1]

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
        map_array(np.ndarray): Map of current field

    Return:
        bool: True if valid position to move to
    """
    rows = len(map_array)
    cols = len(map_array[0])
    if i < 0 or i >= rows:
        return False
    if j < 0 or j >= cols:
        return False
    if map_array[i, j] == OUT_OF_BOUNDS:
        return False
    return True


class PolicyException(Exception):
    """
    User-created exception class for the policy class.
    """

    def __init__(self, message):
        """
        Constructor for the PolicyException class

        Args:
            message (str): Message to display when exception is raised
        """
        self.message = message


class Policy:
    """
    Policy class A current state is entered into the class with the map,
    then an action is made and updated map is returned. Probabilities of 
    actions can vary over time.

    Attributes:
        weights(np.ndarray): weights associated with the policy

    Methods:
        chooseNextState(int, int, np.ndArray, np.ndArray) -> int, int, int
    """

    def __init__(self, weights):
        """
        Constructor for the Policy class

        Args:
            weights (np.ndarray): 1d array representing the weights of probability
                                  for taking a certain action.
        """
        self.weights = np.array(weights)
        for weight in self.weights:
            weight = 0 if weight < 0 else weight

    def chooseNextState(self, x, y, policyMap, mapArray):
        """
        This function takes into account current position and policy to choose
        a next state for the "robot". Note: it is possible for this function to
        be unable to choose a state. In that scenario an exception is thrown.

        Args:
            x (int): current x coordinate
            y (int): current y coordinate
            policyMap (np.ndarray): [description]
            mapArray (np.ndarray): [description]

        Returns:
            int: new x coordinate
            int: new y coordinate
            int: action taken
        """
        new_x, new_y, action = self.__getNewState(x, y)
        while not valid(new_x, new_y, mapArray) and action != -1:
            self.weights[action] = 0
            new_x, new_y, action = self.__getNewState(x, y)
            if action == -1:
                raise PolicyException("Robot is stuck. Please restart.")
        return new_x, new_y, action

    def __getNewState(self, x, y):
        """
        Uses random number generation and policy wait values to determine a new
        state of the system and the action required to transition into that 
        state.

        Args:
            x (int): previous x coordinate
            y ([type]): previous y coordinate

        Returns:
            int: new x coordinate
            int: new y coordinate
            int: number representing proposed action to take
        """
        sumOfAll = self.__sumTotal(NUMBER_OF_ACTIONS)
        if sumOfAll <= 0:
            self.weights = self.weights + 1
            sumOfAll = NUMBER_OF_ACTIONS
        randomNumber = rand.randrange(sumOfAll)

        newX = x
        newY = y
        action = -1
        n = 0
        while n < NUMBER_OF_ACTIONS:
            if randomNumber < self.__sumTotal(n + 1):
                newX, newY, action = x + X_ACTIONS[n], y + Y_ACTIONS[n], n
                n = NUMBER_OF_ACTIONS
            n += 1
        return newX, newY, action

    def __sumTotal(self, numberOfElements):
        """
        Calculates a partial sum of the weights in the set of weights.

        Args:
            numberOfElements (int): number of elements to add up between 1 and 8

        Returns:
            int: partial sum of the elements
        """
        sumTotal = 0
        for n in range(numberOfElements):
            sumTotal += self.weights[n]
        return sumTotal
