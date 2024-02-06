#!/usr/bin/python3
"""
This module provides a function for converting an object to a dictionary
description suitable for JSON serialization.

Functions:
- class_to_json(obj): Convert an object to a JSON-compatible dictionary.
"""


def class_to_json(obj):
    """
    Return a dictionary description with simple data structures\
    for JSON serialization of an object.

    Args:
        obj (object): An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary representing the JSON serialization of the object.
    """
    attributes = obj.__dict__
    serializable_attributes = {}
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value
    return serializable_attributes
