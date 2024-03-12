#!/usr/bin/python3
"""Defines a class BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    """Class BaseGeometry.
    """
    def area(self):
        """Method that defines the area of a geomtric shape

        Raises:
            Exception: if area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that recieves the value property

        Args:
            name: name of the object.
            value: value of the property.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
