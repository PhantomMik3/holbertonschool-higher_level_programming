#!/usr/bin/python3
"""Module: 3-Rectangle"""
"""
Creating a Rectangle class
"""


class Rectangle:
    """Rectangle class we're gonna be working on.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle.
        Parameters:
            width: The width of the Rectangle
            height: The height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width
        Returns: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width
        Parameter:
            value: the width value
        Raises:
            TypeError: if the width is not an integer.
            ValueError: if the width is less than 0.
            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height
        Returns: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height.
        parameter: value: the height value.

        Raises:
            TypeError: if the height is not an integer.
            ValueError: if the height is less than 0
            """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >- 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle.

        Returns: the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns: the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: The rectangle printed by '#'.
            """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle = ""
        for _ in range(self.height):
            rectangle += "#" * self.width + "\n"
        return rectangle[:-1]
