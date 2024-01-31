#!/usr/bin/python3
"""
    Divide all elements of a matrix by a number.

    Parameters:
    - matrix (list of lists): The matrix containing integers or floats.
    - div (int or float): The number to divide all elements of the matrix.

    Returns:
    list of lists: A new matrix where all elements are divided by div and rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats.
    TypeError: If each row of the matrix doesn't have the same size.
    TypeError: If div is not a number (integer or float).
    ZeroDivisionError: If div is equal to 0.
    """

def matrix_divided(matrix, div):
    new_matrix = [[]]

    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate each row has the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]

    return new_matrix
