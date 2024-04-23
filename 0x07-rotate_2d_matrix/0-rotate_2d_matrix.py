#!/usr/bin/python3
"""an n x n 2D matrix"""


def rotate_2d_matrix(matrix):
    """an n x n 2D matrix"""
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    for row in matrix:
        print(' '.join(map(str, row)))
