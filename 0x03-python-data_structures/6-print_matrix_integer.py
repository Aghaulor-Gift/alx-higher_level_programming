#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if matrix[i]:
            print(" ".join("{:d}".format(num) for num in matrix[i]))
        else:
            print()
