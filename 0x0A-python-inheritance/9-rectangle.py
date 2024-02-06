#!/usr/bin/python3
"""A moduule that defines a class with area and integer_validator methods."""


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
