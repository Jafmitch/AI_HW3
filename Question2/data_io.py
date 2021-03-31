
"""
- File: data_io.py
- Author: Jason A. F. Mitchell
- Summary: This module is for imputing and outputing files. This includes 
           things like outputing figures based on data used in the overall
           program.
"""

import graph_wrapper as gw

# Macros for map array
OUT_OF_BOUNDS = -1
EMPTY = 0
START = 1
CURRENT = 2
END = 3

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
            elif mapArray[x][y] == CURRENT:
                plot.addPoint(x, y, style="o", color="purple")

    # draw route
    X = 0
    Y = 1
    for i in range(len(route) - 1):
        plot.addLine(route[i][X], route[i][Y],
                     route[i + 1][X], route[i + 1][Y], "blue")

    plot.setAxis(False)
    # plot.label("Route Taken")
    # plot.save("route.jpg")
    # plot.freeze()
    plot.display()
