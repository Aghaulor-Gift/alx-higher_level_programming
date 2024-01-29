#!/usr/bin/python3
"""A module that defines a rectangle"""


class Rectangle:
    """
    A class representing a rectangle with width and height attribute."""

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle with the given width and height.

        Parameters:
        - width (int): Width of the rectangle initialised to 0.
        - height (int): Height of the rectangle initialised to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
        - value (int): The new value for the width attribute.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Parameters:
        - value (int): The new value for the height attribute.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
