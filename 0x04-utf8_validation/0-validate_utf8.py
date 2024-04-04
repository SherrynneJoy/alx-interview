#!/usr/bin/python3
"""a method that determines if a given data set represents a valid
UTF-8 encoding"""


def validUTF8(data):
    """a method that determines if a given data set represents a valid UTF-8
    encoding"""
    i = 0
    while i < len(data):
        leading_bytes = 0
        mask = 1 << 7
        while mask & data[i]:
            leading_bytes += 1
            mask >>= 1
        if leading_bytes == 0:
            i += 1
            continue
        if leading_bytes == 1 or leading_bytes > 4:
            return False
        trailing_bytes = leading_bytes - 1
        i += 1
        while trailing_bytes > 0:
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
            i += 1
            trailing_bytes -= 1
    return True
