#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in range(len(matrix)):
        new_row = list(map(lambda x: x ** 2, matrix[row]))
        result.append(new_row)
    return result
