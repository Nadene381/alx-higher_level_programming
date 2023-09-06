#!/usr/bin/python3
"""
   This module defines a rectangle class
"""


class Rectangle:
    """
    This class represents a Rectangle.

    """
    pass

"""
This module represents a rectangle class
"""


class Rectangle:
    """
    This class represents a rectangle width and height attributes are added.

    Attributes:
        width: The width of the rectangle.
        height: The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Rectangle instance with (width and height that are optional).

        Arguments:
            width: The width of the rectangle.
            height: The height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
        The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value: The width to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value: The height to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
