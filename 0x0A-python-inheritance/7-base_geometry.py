#!/usr/bin/python3
'''
    An empty class
'''


class BaseGeometry():
    '''
       Class that represents a BaseGeometry class
    '''
    def area(self):
        '''
           A method to raise an exception if area was not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
            A method to validate the value
            Raise TypeError and ValueError
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
