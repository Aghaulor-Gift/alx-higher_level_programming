#!/usr/bin/python3
"""Multiply two matrices.
Parameters:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    """
    
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not m_a or any(not isinstance(row, list) for row in m_a) or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")

    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not m_b or any(not isinstance(row, list) for row in m_b) or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
        for row_a in m_a
    ]

    return result_matrix
