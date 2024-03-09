#!/usr/bin/python3
"""Creating Pascal's Triangle"""


def pascal_triangle(n):
    myValues = []
    if n <= 0:
        return myValues
    myValues = [[1]]

    for i in range(1, n):
        new = [1]
        for j in range(len(myValues[i - 1]) - 1):
            new.append(myValues[i - 1][j] + myValues[i - 1][j + 1])
        new.append(1)
        myValues.append(new)
    return myValues
