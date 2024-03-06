#!/usr/bin/python3
'''ALX 2D matrix proj'''


def rotate_2d_matrix(matrix):
    '''this module rotates a 2d matrix 90° clockwise
    Returns: Nothing'''
    left, right = 0, len(matrix) - 1

    while left < right:
        for j in range(right - left):
            top, bottom = left, right
            # save topleft  value
            topLeft = matrix[top][left + j]
            # move bottom left to top left
            matrix[top][left + j] = matrix[bottom - j][left]
            # move bottom right to bottom left
            matrix[bottom - j][left] = matrix[bottom][right - j]
            # move top right to bottom right
            matrix[bottom][right - j] = matrix[top + j][right]
            # move top left to top right
            matrix[top + j][right] = topLeft
        right -= 1
        left += 1
