import os
import time
import math


def progress(i, numOfRan):
    rows, columns = os.popen('stty size', 'r').read().split()
    percentage = math.floor((i/numOfRan)*100)
    percentageStr = str(percentage) + "% "

    if len(percentageStr) == 3:
        tf = 5
    elif len(percentageStr) == 4:
        tf = 6
    else:
        tf = 7

    lengthOfSpace = int(columns)-tf
    barPercentages = math.floor((i/numOfRan) * lengthOfSpace)
    equalsSign = "=" * barPercentages
    spaces = " " * ((int(columns) - barPercentages) - tf)

    if (i + 1) == numOfRan:
        print("100% [" + equalsSign + "]")
    else:
        print(percentageStr + "[" + equalsSign + spaces + "]", end="\r")
