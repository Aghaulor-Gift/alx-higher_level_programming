#!/usr/bin/python3
"""A module representing a rectangle"""


class Rectangle:
    """
    A class representing a rectangle with width and height attributes.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle with the given width and height.

        Parameters:
        - width (int): Width of the rectangle (default is 0).
        - height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
        - int: Perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        A string representation of the rectangle using the print_symbol.

        Returns:
        - str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += str(self.print_symbol) * self.__width + "\n"
            return rectangle_str.rstrip()

    def __repr__(self):
        """
        A str representation of the rectangle for recreation using eval().

        Returns:
        - str: String representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a deletion message."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rectangle based on the area.

        Parameters:
        - rect_1: An instance of Rectangle.
        - rect_2: An instance of Rectangle.

        Raises:
        - TypeError: If rect_1 is not an instance of Rectangle.
        - TypeError: If rect_2 is not an instance of Rectangle.

        Returns:
        - Rectangle: The bigger rectangle, or rect_1 if both have\
          the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
