#!/usr/bin/python3
"""Module that contains class base"""


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing instances"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_obnects
