#!/usr/bin/python3
"""Module that contains the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def ___init__(self, width, height, x=0, y=0, id=None):
        """initializing instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("Height is not an integer")
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x is not an integer")
        if value <= 0:
            raise ValueError("x must be greater than 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y is not an integer")
        if value <= 0:
            raise ValueError("y must be greater than 0")
        self.__y = value
