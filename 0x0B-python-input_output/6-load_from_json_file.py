#!/usr/bin/python3
"""Defines a module for loading an object from a JSON file."""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        obj: The object loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
