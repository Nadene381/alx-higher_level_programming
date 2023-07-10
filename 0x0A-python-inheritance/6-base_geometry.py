#!/usr/bin/python3
'''
    Class empty
'''


class BaseGeometry():
    '''
        Represents a BaseGeometry class
    '''
    def area(self):
        '''
            function that raise exception if area 
            was not implemented
        '''
        raise Exception("area() is not implemented")
