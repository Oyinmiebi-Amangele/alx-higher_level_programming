#!/usr/bin/python3
"""A class that defines a Rectangle"""


class Rectangle:
    """Representation of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the rectangle parameter.
        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set of the width parameter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set of the height parameter"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that finds the area
        Return: area """

        return (self.__width * self.__height)

    def perimeter(self):
        """Function that finds the perimeter
        Return: perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Method of returning the string
        representation as #
        Returns: the string representation#"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += ("#" * self.width) + "\n"
        return string[:-1]
