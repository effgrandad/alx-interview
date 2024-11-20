#!/usr/bin/python3
"""
2D Matrix, rotatation module.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list): The input 2D matrix.

    Returns:
        None: The function modifies the matrix in-place.
    """
    matrix_size = len(matrix)

    # Reverse the matrix
    for row_index in range(matrix_size):
        for col_index in range(row_index, matrix_size):
            matrix[row_index][col_index], matrix[col_index][row_index] = \
                matrix[col_index][row_index], matrix[row_index][col_index]

    # Reverse each row
    for row in matrix:
        row.reverse()
