#!/usr/bin/python3
"""A class that defines a Rectangle"""


class Rectangle:
    """Represent the Rectangle"""

    def __init___(self, width=0, height=0):
        """Initializing the rectangle.
        Args:
            width(int): width of the rectangle.
            height(int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the property of the width"""
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
        """Get/set the property of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function to find the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Function to find the perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)

            return (2 * (self.width + self.height))
