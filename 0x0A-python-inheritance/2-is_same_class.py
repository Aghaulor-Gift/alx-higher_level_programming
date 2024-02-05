#!/usr/bin/python3
"""A module that returns the exact instance of the class"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise, returns False.
    """

    return type(obj) == a_class
