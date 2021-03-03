# graph_wrapper.py
# written by Jason A. F. Mitchell
# last updated: 2/7/2021

import matplotlib.pyplot as plt

STEP_SIZE = 0.001


class Plot:
    def __init__(self):
        self._bars = []
        self._lines = []
        self._points = []
        self._text = []
        self.delayTime = 0.1

    def __del__(self):
        self.clear()

    def addBarGraph(self, xVals, yVals):
        self._bars.append(plt.bar(xVals, yVals))

    def addFunction(self,
                    function,
                    xMin=0,
                    xMax=0,
                    color="red",
                    stepSize=STEP_SIZE):
        newLine = [[], []]
        index = 0
        x = xMin
        while x < xMax:
            newLine[0].append(x)
            newLine[1].append(function(x))
            x += stepSize
            index += 1
        self._lines.append(plt.plot(newLine[0], newLine[1], color=color))

    def addLegendLabel(self, objectType="line", index=-1, label=""):
        objectArray = []
        if objectType == "point":
            objectArray = self._points
        else:
            objectArray = self._lines
        if index == -1:
            index = len(objectArray) - 1
        objectArray[index][0].set_label(label)

    def addLine(self, x1=0, y1=0, x2=0, y2=0, color="red"):
        self._lines.append(plt.plot([x1, x2], [y1, y2], color=color))

    def addPoint(self, xVal=0, yVal=0, style="o", color="blue"):
        self._points.append(
            plt.plot(xVal, yVal, marker=style, color=color)
        )

    def addText(self, xVal=0, yVal=0, message=""):
        self._text.append(plt.text(xVal, yVal, message))

    def clear(self):
        while len(self._lines) > 0:
            self.removeLine()
        while len(self._points) > 0:
            self.removePoint()
        while len(self._text) > 0:
            self.removeText()

    def display(self):
        plt.pause(self.delayTime)

    def freeze(self):
        plt.show()

    def label(self, title="", xLabel="", yLabel=""):
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)

    def pointplot(self, xArray, yArray, color="red"):
        self._lines.append(plt.plot(xArray, yArray, color=color))

    def removeBarGraph(self, index=-1):
        self._bars.pop(index).remove()

    def removeLine(self, index=-1):
        self._lines.pop(index).pop().remove()

    def removePoint(self, index=-1):
        self._points.pop(index).pop().remove()

    def removeText(self, index=-1):
        self._text.pop(index).remove()

    def save(self, name="plot.jpeg"):
        plt.savefig("images/" + name)

    def setAxis(self, value=True):
        plt.axis(value)

    def showLegend(self):
        plt.legend()
