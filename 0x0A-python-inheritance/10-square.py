#!/usr/bin/python3
'''9-base_geometry.py'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
