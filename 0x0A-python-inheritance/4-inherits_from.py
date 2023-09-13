#!/usr/bin/python3
""" Objects that describes inheritance"""


def inherits_from(obj, a_class):
    """function that returns true if object is an
    instance of a class that inherited from the
    specified class.
    Args:
        obj: the object concerned.
        a_class: the target class.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
