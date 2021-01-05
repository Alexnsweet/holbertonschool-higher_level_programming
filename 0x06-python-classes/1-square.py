#!/usr/bin/python3
"""
    This is an example of private instance attributes
"""


class Square:
    """
        This class creates a square with instatiation of size
    """"
    def __init__(self, size):
        self.__size = size
