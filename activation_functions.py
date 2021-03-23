"""
- File: activation_functions.py
- Author: Jason A. F. Mitchell
- Summary: This module has some common activation functions for neural networks.
"""

import numpy as np

def relu(xArray):
    """
    Calculates y = relu(x)

    Args:
        xArray (ndarray): Array of x values.

    Returns:
        ndarray: Array of y values.
    """
    return np.maximum(xArray, 0)

def reluPrime(xArray):
    """
    Calculates y = relu'(x) or y = Heaviside(x)

    Args:
        xArray (ndarray): Array of x values.

    Returns:
        ndarray: Array of y values.
    """
    yArray = []
    for x in xArray:
        yArray.append(1 if x >= 0 else 0)
    return np.array(yArray)
