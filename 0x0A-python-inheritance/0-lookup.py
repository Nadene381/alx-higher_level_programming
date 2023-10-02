#!/usr/bin/python3
'''
    A Function that returns a list of attributes or methods available
'''


def lookup(obj):
    '''
    A Function that returns attributes of objector instance
    '''
    return (dir(obj))
