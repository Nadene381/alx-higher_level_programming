
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon July 31 19:27 2023

@author: Nadene Samuels
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    A Square class shape, inheirts from BaseGeometry
    """
    def __init__(self, size):
        """"
        A function for Square

        Attributes:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        A funtion to print with/height

        Returns:
            Return width/height
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """
        A function that calculates the area of the Square
        """
        return self.__size ** 2
