#!/usr/bin/python3
"""Module: 8-Rectangle"""
"""
Creating a Rectangle class
"""


class Rectangle:
    """Rectangle class we're gonna be working on.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle.
        Parameters:
            width: The width of the Rectangle
            height: The height of the Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            rectangle += str(self.print_symbol) * self.width + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """Returns a string representation of a rectangle.

        Returns: str: a string representation of a rectangle

        """
        return f"Rectangle{self.width}, {self.height}"

    def __del__(self):
        """Prints a farewell message when rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle

        Parameters:
            rect_1: first rectangle
            rect_2: second rectangle

        Raises:
            TypeError: if rect_1 is not an instance of Rectangle
            TypeError: if rect_2 is not an instance of Rectangle

        Returns:
            Rectangle: the rectangle with the biggest area
            """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
