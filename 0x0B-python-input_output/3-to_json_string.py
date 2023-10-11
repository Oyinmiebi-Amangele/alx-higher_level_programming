#!/usr/bin/python3
"""Module that contains the function that converts
an object(string) to json."""
import json


def to_json_string(my_obj):
    """Funtion that converts an object to json
    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded
    """

    obj = json.dumps(my_obj)
    return obj
