#!/usr/bin/python3
""" Defining an object check """


def is_kind_of_class(obj, a_class):
    """ A function that checks if an object is an instance
    of a class.
    Args:
        obj: the object to check
        a_class: the type to accertain with.
    Return: Return True if it is an instance.Otherwise,
        False.
    """
    return isinstance(obj, a_class)
