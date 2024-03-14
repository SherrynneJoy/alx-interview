#!/usr/bin/python3
"""uses a key retrieved from one box to open closed boxes"""


def canUnlockAll(boxes):
    """using lists to retrieve keys that will unlock boxes"""
    m = len(boxes)
    unlocked = [False] * m
    unlocked[0] = True
    keys = set(boxes[0])
    while keys:
        key = keys.pop()
        if 0 <= key < m and not unlocked[key]:
            unlocked[key] = True
            keys.update(boxes[key])
    return all(unlocked)
