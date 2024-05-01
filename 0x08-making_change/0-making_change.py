#!/usr/bin/python3
"""the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """fewest number of coins needed to meet a given amount total"""
    count = [float('inf')] * (total + 1)
    count[0] = 0

    for i in range(1, total + 1):
        for c in coins:
            if i - c >= 0:
                count[i] = min(count[i], 1 + count[i - c])

    if count[total] == float('inf'):
        return -1
    else:
        return count[total]
