#!/usr/bin/python3
""" a method that calculates the fewest number of operations needed to result
in exactly n H characters in the file."""


def minOperations(n):
    """calculates the fewest number of operations needed to result in
    exactly n H characters in the file."""
    if n < 2:
        return 0
    myArr = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                myArr.append(i)
    return sum(myArr)
