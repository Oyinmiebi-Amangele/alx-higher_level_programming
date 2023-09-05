#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Method that initialized the instance
        Args:
            width: rectangle width
            height: rectangle height

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that returns the value of the width
        Returns:
            rectangle width
            """
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
        """method that returns the value of the height
        Returns:
            rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that calculates the Rectangle area
        Returns:
            rectangle area
            """
        return self.width * self.height

    def perimeter(self):
        """Method that calculates the Rectangle perimeter
        Returns:
            rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) * (2 * self.height)

    def __str__(self):
        """Method that returns the Rectangle #

        Returns:
            str of the rectangle

        """
        string = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns the string representation of the instance
        Returns:
            string representation of the object
            """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
