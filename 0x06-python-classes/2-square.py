#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """
        Initializes a square with an optional specified size.

        Args:
            size (int, optional): Size of the square (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
