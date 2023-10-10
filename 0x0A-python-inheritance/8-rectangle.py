#!/usr/bin/python3
""" Creating a class Rectangle from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defining the properties of a Rectangle."""

    def __init__(self, width, height):
        """initializing the width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
