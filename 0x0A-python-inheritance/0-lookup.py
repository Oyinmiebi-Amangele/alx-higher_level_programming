#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of
    an object.

    Args:
        obj(object): The object to inspect.

    Return:
        List: A list of attribute and method names.
    """
    return dir(obj)
