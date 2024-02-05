#!/usr/bin/python3
"""
A module that defines a base geometry
"""


class BaseGeometry:
    """
    A class with area and integer_validator methods
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
