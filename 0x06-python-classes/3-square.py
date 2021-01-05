#!/usr/bin/python3

"""
    This is an example of validation
"""


class Square:
    """
        This class creates a square with instatiation of size with validation
    """
    def __init__(self, size=0):
        """
        Initializes private attribute size
        Check if size is int and >=0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
    def area(self):
        """
            Method that defines area of square by squaring size
        """
        return (self.__size * self.__size)
