# hw3.py
# written by Jason A. F. Mitchell and Eric Tulowetzke
# last updated: 3/3/2021

import graph_wrapper as gw


def main():
    graphTestingData()


def graphTestingData():
    plot = gw.Plot()
    with open('testdata.dat') as f:
        for line in f.read().split("\n"):
            data = line.split(",")
            if len(data) == 3:
                if int(data[2].strip()) == 1:
                    plot.addPoint(float(data[0].strip()), float(
                        data[1].strip()), "o", "blue")
                else:
                    plot.addPoint(float(data[0].strip()), float(
                        data[1].strip()), "o", "red")

    plot.label("Test Data",  "x", "y")
    plot.save("test_data.jpg")
    plot.freeze()


if __name__ == "__main__":
    main()
