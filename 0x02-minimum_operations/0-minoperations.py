#!/usr/bin/python3
""" a method that calculates the fewest number of operations needed to result
in exactly n H characters in the file."""


def minOperations(n):
    """calculates the fewest number of operations needed to result in
    exactly n H characters in the file."""
    if n <= 0:
        return 0
    myArr = [0] * (n + 1)
    for i in range(2, n + 1):
        myArr[i] = i
        for j in range(2, i):
            if i % j == 0:
                myArr[i] = min(myArr[i], myArr[j] + i // j)
    return myArr[n]
