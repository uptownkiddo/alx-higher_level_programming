#!/usr/bin/python3

class Rectangle:
    '''Class the defines a rectangle'''
    #public class attribute
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initialises the rectangle
        width and height have a default value of 0'''
        self.__width = width
        self.__height = height

        type( self ).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance( value, int ) is False:
            raise TypeError( 'width must be an integer' )
        if value < 0:
            raise ValueError( 'width must be >= 0' )

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance( value, int ) is False:
            raise TypeError( 'height must be an integer' )
        if value < 0:
            raise ValueError( 'height must be >= 0' )

        self.__height = value

    def area(self):
        '''Calculates the area '''
        area = self.__width * self.__height
        return area

    def perimeter(self):
        '''Calculates the perimeter'''
        if self.__height | self.__width == 0:
            perimeter = 0
            return perimeter
        else:
            perimeter = (self.__width + self.__height) * 2
            return perimeter

    def __str__(self):
        string = ''
        if self.__width | self.__height == 0:
            return string
        else:
            for i in range( self.__height ):
                for j in range( self.__width ):
                    string += str(self.print_symbol)
                if i is not self.__height - 1:
                    string += '\n'

            return string

    def __repr__(self):
        return ('Rectangle ({}, {})'.format( self.__width, self.__height ))

    def __del__(self):
        '''deletes a rectangle instance'''
        type( self ).number_of_instances -= 1
        print( 'Bye rectangle...' )

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the biggest rectangle based on area'''

        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        '''Return a new rectangle instance with width == height ==size'''
        return cls(size, size)



