#!/usr/bin/python3
'''Salam'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

if __name__ == "__main__":
    print(issubclass(Rectangle, BaseGeometry))
    s = Square(5)
    print(s)
    print(s.area())
