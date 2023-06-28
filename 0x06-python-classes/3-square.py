#!/usr/bin/python3
'''
This module consist of a class that defines a square.
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        Calculate and returns the area of a square.
        Returns:
            int: The area of the square.
        '''
        return self.__size ** 2
