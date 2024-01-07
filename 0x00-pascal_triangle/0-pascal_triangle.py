#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    p_triangle = [0] * n

    for i in range(n):
        # define a row and fill first and last idx with 1
        new_row = [0] * (i+1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = p_triangle[i - 1][j]
                b = p_triangle[i - 1][j - 1]
                new_row[j] = a + b

        p_triangle[i] = new_row

    return p_triangle
