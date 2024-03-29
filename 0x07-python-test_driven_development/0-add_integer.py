#!/usr/bin/python3
"""A module that add integers
Parameters:
    - a (int or float): The first number.
    - b (int or float, optional): The second number. Defaults to 98.
"""

def add_integer(a, b=98):
    """
    Adds two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
