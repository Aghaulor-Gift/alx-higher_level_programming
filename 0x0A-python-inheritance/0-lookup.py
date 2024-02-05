#!/usr/bin/python3
"""
    Returns a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Represent the lookup function that searches throught the list.
    """
    return [attr for attr in dir(obj)]
