#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialice the values """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area for rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Returns the area for rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """ Redefine the method str to print the rectangle
            with given symbol
        """
        cadena = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                cadena += str(self.print_symbol) * self.width
                if i < (self.height - 1):
                    cadena += "\n"

        return cadena

    def __repr__(self):
        """ Redefine the method repr to allow to create new instancies of the
            class, but with same values
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
