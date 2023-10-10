#!/usr/bin/python3
""" Defining a class BaseGeometry."""


class BaseGeometry:
    """Creating the properties of the BaseGeometry."""

    def area(self):
        """area not yet implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates the integer.
        Args:
            name(str):name of the parameter.
            value(int):parameter to be validated.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
