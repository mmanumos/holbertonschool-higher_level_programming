#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        try:
            self.position = position
        except TypeError as ti:
            print(ti)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) != tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        ''' Returns the area '''
        return self.__size * self.__size

    def my_print(self):
        '''print the square '''
        if self.__size == 0:
            print()

        for k in range(self.position[1]):
            print()

        for i in range(self.__size):
            for h in range(self.position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
