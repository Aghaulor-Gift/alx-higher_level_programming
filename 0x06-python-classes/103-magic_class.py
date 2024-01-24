#!/usr/bin/python3
"""Defines magic class from a given ByteCode"""
import math


class MagicClass:
    """Represent the magicclass"""

    def __init__(self, radius=0):
        """
        Initialization of the MagicClass
        Arg:
        radius(int,float):radius initialised to 0.
        """

        if type(radius) not in (int, float) or type(radius)
        is float and radius.is_integer() is False:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculate the area of the magic class
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the area of the magic class
        """
        return 2 * math.pi * self.__radius
