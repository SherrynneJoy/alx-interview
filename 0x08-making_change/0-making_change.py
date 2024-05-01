#!/usr/bin/python3
"""the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
