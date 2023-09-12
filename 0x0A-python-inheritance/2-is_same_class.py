#!/usr/bin/python3
""" Defines a class checking function"""


def is_same_class(obj, a_class):
    """ function that checkes if the obj is
    a an instance of a class"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
