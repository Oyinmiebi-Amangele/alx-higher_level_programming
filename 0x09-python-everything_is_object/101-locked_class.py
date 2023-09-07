#!/usr/bin/python3
"""
This a module that contains a class that avoides dynamically created attributes
"""

class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
