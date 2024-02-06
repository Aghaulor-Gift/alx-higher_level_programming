#!/usr/bin/python3
"""JSON Representation Module

This module provides a function to_json_string to convert Python objects
into their JSON representation.
"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object."""
    return json.dumps(my_obj)
