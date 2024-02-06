#!/usr/bin/python3
"""A module that defines a function that adds new attribute to an object
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception if the object can't have a new attribute.

    Parameters:
    - obj: The object to which the attribute should be added.
    - attr: The name of the attribute.
    - value: The value of the attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
