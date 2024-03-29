#!/usr/bin/python3
""" A module that prints a message with the given first and last names.
    Parameters:
    - first_name (str): The first name.
    - last_name (str): The last name. Defaults to an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.
"""


def say_my_name(first_name, last_name=""):
    """Prints a message with the given first and last names"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
