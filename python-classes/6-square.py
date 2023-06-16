#!/usr/bin/python3

"""
module: 6-square
class Square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        define size to square and position
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        return area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        printing output
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)

    @property
    def size(self):
        """
        returning size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        defining size to square if value is
        an int and bigger than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        returning position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
