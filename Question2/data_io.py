
"""
- File: data_io.py
- Author: Jason A. F. Mitchell
- Summary: This module is for imputing and outputing files. This includes 
           things like outputing figures based on data used in the overall
           program.
"""

import graph_wrapper as gw
import numpy as np


def printMap(mapArray):
    xLen = len(mapArray)
    yLen = len(mapArray[0])
    plot = gw.Plot()
    for x in range(xLen):
        plot.addLine(x, yLen - 1, x, 0, color="gray")
    for y in range(yLen):
        plot.addLine(0, y, xLen - 1, y, color="gray")
    for x in range(xLen):
        for y in range(yLen):
            if mapArray[x][y] == 1:
                plot.addPoint(x, y, style="o", color="blue")
            elif mapArray[x][y] == -1:
                plot.addPoint(x, y, style="o", color="red")
            elif mapArray[x][y] == 2:
                plot.addPoint(x, y, style="o", color="green")
    plot.setAxis(False)
    plot.freeze()
