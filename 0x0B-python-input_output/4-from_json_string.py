#!/usr/bin/python3
"""Module that contains a function that converts
a json representation to a python representation"""
import json


def from_json_string(my_str):
    """function that converts json representation
    to python representation
     Args:
        my_str: JSON representation

    Raises:
        Exception: when the string can't be decoded
    """
    return (json.loads(my_str))
