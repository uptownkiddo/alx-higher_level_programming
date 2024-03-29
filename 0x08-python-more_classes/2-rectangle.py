#!/usr/bin/python3
'''Rectangle module'''


class Rectangle:
    '''Creates a rectangle'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        '''Returns the area of the rectangle'''
        area = self.__width * self.__height
        return area
    def perimeter(self):
        '''Returns the perimeter of the rectangle'''
        if self.__height | self.__width == 0:
            perimeter = 0
            return perimeter
        else:
            perimeter = (self.__width + self.__height)*2
            return perimeter
