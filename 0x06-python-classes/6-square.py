#!/usr/bin/python3

"""
    This is an example of validation
"""


class Square:
    """
        This class creates a square with instatiation of size with validation
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes private attribute size
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
            Attribute to retrieve
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
            Setter to initialize value
        """
        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
            Method that defines area of square by squaring size
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
            Method that prints square
        """
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("{}{}".format((' '*self.__position[0]), ('#'*self.__size)))
