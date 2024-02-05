#!/usr/bin/python3
"""
A module that defines a base geometry
"""


class BaseGeometry:
    """A class with an unimplemented area method."""

    def area(self):
        """Raises an Exception 'area() is not implemented'."""
        raise Exception("area() is not implemented")
