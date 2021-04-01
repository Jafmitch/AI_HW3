
"""
- File: data_io.py
- Author: Jason A. F. Mitchell
- Summary: This module is for imputing and outputing files. This includes 
           things like outputing figures based on data used in the overall
           program.
"""

import graph_wrapper as gw

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


def displayMap(mapArray, currentLocation):
    """
    Displays visual of map array using graph wrapper. Will also display a point
    at the current location of the "robot".

    Args:
        mapArray (list): 2d list representing the map of the problem
        currentLocation (tuple): Current location represented as x and y coordinates
    """
    xLen = len(mapArray)
    yLen = len(mapArray[0])
    plot = gw.Plot()

    # draw lines
    for x in range(xLen):
        plot.addLine(x, yLen - 1, x, 0, color="gray")
    for y in range(yLen):
        plot.addLine(0, y, xLen - 1, y, color="gray")

    # draw dots
    for x in range(xLen):
        for y in range(yLen):
            if mapArray[x][y] == START:
                plot.addPoint(x, y, style="o", color="blue")
            elif mapArray[x][y] == OUT_OF_BOUNDS:
                plot.addPoint(x, y, style="o", color="red")
            elif mapArray[x][y] == END:
                plot.addPoint(x, y, style="o", color="green")
    plot.addPoint(currentLocation[X],
                  currentLocation[Y], style="o", color="purple")

    plot.setAxis(False)
    plot.display()


def printDistancesTraveled(distancesTraveled):
    """
    This function prints a graph of the total distances traveled in each iteration
    of the algorithm.

    Args:
        distancesTraveled (list): List of floats representing the total distance
                                  traveled at each iteration.
    """
    plot = gw.Plot()
    plot.pointplot(range(len(distancesTraveled)), distancesTraveled)
    plot.label("Distance Traveled vs. Iteration",
               "Iteration", "Distance Traveled")
    plot.save("distance_traveled.jpg")
    plot.freeze()


def printMap(mapArray, route):
    """
    Prints visual of map array using graph wrapper. Will also display a route
    taken when given a list of coordinates.

    Args:
        mapArray (list): 2d list of integers representing map of problem.
        route (list, optional): List of coordinates representing the route
                                taken. Defaults to None.
    """
    xLen = len(mapArray)
    yLen = len(mapArray[0])
    plot = gw.Plot()

    # draw lines
    for x in range(xLen):
        plot.addLine(x, yLen - 1, x, 0, color="gray")
    for y in range(yLen):
        plot.addLine(0, y, xLen - 1, y, color="gray")

    # draw dots
    for x in range(xLen):
        for y in range(yLen):
            if mapArray[x][y] == START:
                plot.addPoint(x, y, style="o", color="blue")
            elif mapArray[x][y] == OUT_OF_BOUNDS:
                plot.addPoint(x, y, style="o", color="red")
            elif mapArray[x][y] == END:
                plot.addPoint(x, y, style="o", color="green")

    # draw route
    X = 0
    Y = 1
    for i in range(len(route) - 1):
        plot.addLine(route[i][X], route[i][Y],
                     route[i + 1][X], route[i + 1][Y], "blue")

    plot.setAxis(False)
    plot.label("Route Taken")
    plot.save("route.jpg")
    plot.freeze()


def printPolicyMap(policyMap):
    """
    Create a visual of the policy map using different colored lines.

    Args:
        policyMap (list): 3d list representing the policy map
    """
    plot = gw.Plot()

    for x in range(len(policyMap)):
        for y in range(len(policyMap[0])):
            for action in range(len(policyMap[0][0])):
                colorVal = int(policyMap[x][y][action] * (255/1000))
                colorVal = 16 if colorVal < 16 else colorVal
                colorVal = 255 if colorVal > 255 else colorVal
                plot.addLine(
                    x,
                    y,
                    x + 0.5 * X_ACTIONS[action],
                    y + 0.5 * Y_ACTIONS[action],
                    color="#" + hex(colorVal)
                    .replace("0x", "")[0:2].upper() + "00FF"
                )

    plot.setAxis(False)
    plot.label("Policy Map")
    plot.save("Policy Map.jpg")
    plot.freeze()
