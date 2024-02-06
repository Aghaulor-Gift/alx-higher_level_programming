#!/usr/bin/python3
"""
Pascal's Triangle Generator

This module contains a function to generate Pascal's\
triangle up to a specified number of rows.

Functions:
    pascal_triangle(n): Generate Pascal's triangle up to the nth row.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
