#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """
    A subclass of list
    """
    def __init__(self):
        """initializing the subclass of list"""
        super().__init__()

    def print_sorted(self):
        """function that prints the sorted out list"""
        print(sorted(self))
