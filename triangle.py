# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:59:56 2024

@author: banerm
"""

"""
This module defines a RightTriangle class to represent a right triangle
with specified height and width.
"""



class RightTriangle:
    """
    A class to represent a right triangle.

    Attributes:
    ----------
    _h : float
        Height of the triangle.
    _w : float
        Width of the triangle.
    num_sides : int
        Number of sides of the triangle (always 3).

    Methods:
    -------
    __init__(height, width):
        Initializes a RightTriangle instance with given height and width.
    calc_area():
        Calculates and returns the area of the triangle.
    calc_perimeter():
        Calculates and returns the perimeter of the triangle.
    """

    _num_sides = 3  

    def __init__(self, height, width):
        """
        Initializes a RightTriangle instance.

        Parameters:
        ----------
        height : float
            The height of the right triangle.
        width : float
            The width of the right triangle.

        Raises:
        ------
        ValueError: If height or width is negative.
        """
        if height < 0 or width < 0:
            raise ValueError("Height and width must be non-negative values.")
        
        self._h = height
        self._w = width

    def calc_area(self):
        """
        Calculates the area of the right triangle.

        Returns:
        -------
        float
            The area of the triangle calculated using the formula: 
            (1/2) * height * width.
        """
        return 0.5 * self._h * self._w

    def calc_perimeter(self):
        """
        Calculates the perimeter of the right triangle.

        Returns:
        -------
        float
            The perimeter of the triangle calculated as the sum of 
            all sides: height + width + hypotenuse.
        """
        hypotenuse = (self._h ** 2 + self._w ** 2) ** 0.5
        return self._h + self._w + hypotenuse
    