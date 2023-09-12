#!/usr/bin/python3
""" Defines a class checking function"""


def is_same_class(obj, a_class):
    """ function that checkes if the obj is
    a an instance of a class"""
    return type(obj) is a_class
