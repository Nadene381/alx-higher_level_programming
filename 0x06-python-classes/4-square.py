#!/usr/bin/python3
'''
This module contains a class that defines a square.
'''


class Square:
    """
    This empty class represents a square.
    """

    def __init__(self, size=0):
        '''
        Initialize a new instance of the above square class.
        Args:
            size (int): The size of the square. Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        self.size = size

    @property
    def size(self):
        '''
        Retrieves the size of the square.
        Returns:
            int: The size of the square.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Sets the size of the square.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        Calculates and returns the area of a square.
        Returns:
            int: The area of the square.
        '''
        return self.__size ** 2
