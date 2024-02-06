#!/usr/bin/python3
"""Defines a square that inherits from a rectangle that prints the
description of the square and return square of the square
"""


class BaseGeometry:
    """A class with area and integer_validator methods."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer: raises a TypeError
        - If value is less or equal to 0: raises a ValueError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """
        Initializes a rectangle with a given width and height.

        Parameters:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Parameters:
        - size: The size of the square.
        """
        super().__init__(size, size)
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
