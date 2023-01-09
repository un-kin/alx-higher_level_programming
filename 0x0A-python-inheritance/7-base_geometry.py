#!/usr/bin/python3
'''
Class BaseGeometry
'''


class BaseGeometry:
    '''
    Base class
    '''
    def area(self):
        '''
        Function that raises exception for missing area
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Function that validates value
        '''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
