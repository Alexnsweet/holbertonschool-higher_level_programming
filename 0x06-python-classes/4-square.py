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
        """
        self.__size = size

    @property
    def size(self):
        """
            Attribute to retrieve
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
            Setter to initialize value
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
            Method that defines area of square by squaring size
        """
        return (self.__size * self.__size)
