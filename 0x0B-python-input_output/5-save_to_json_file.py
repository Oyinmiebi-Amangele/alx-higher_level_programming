#!/usr/bin/python3
"""Module that contain a function that writes a
json representation into a textfile"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes a json representation
    into a textfile
     Args:
        my_obj: object
        filename: textfile name

    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, "w", encoding='utf-8') as f:
        return json.dumps(my_obj, f)
