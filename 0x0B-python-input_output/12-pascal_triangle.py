#!/usr/bin/python3
"""pascal_triangle module."""


def pascal_triangle(n):
    """ Function that returns the pascal triangle

    Args:
        n: number of lines

    Returns:
        matrix: a matrix with the pascal triangle

    """
    if n <= 0:
        return []

    res = [[1]]
    while len(res) is not n:
        mat = [1]
        for i in range(len(res[-1]) - 1):
            mat.append(res[-1][i] + res[-1][i + 1])
        mat.append(1)
        res.append(mat)
    return res
