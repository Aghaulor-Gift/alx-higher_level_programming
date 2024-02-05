#!/usr/bin/python3
"""A module that defines the class inherits_from"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; 
    otherwise, returns False.
    """

    return issubclass(type(obj), a_class)
