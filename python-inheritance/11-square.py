#!/usr/bin/python3
"""Module that defines Square class"""

Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """Return string representation: [Square] <width>/<height>"""
        return f"[Square] {self.__size}/{self.__size}"
