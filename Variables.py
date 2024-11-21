# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:10:13 2024

@author: banerm
"""

from math import pi
radius = 1.0
triangle_length = 0.75
triangle_area = (triangle_length **2) / 2 #half square
rectangle_length = 2.0
rectangle_width = 0.75
rectangle_area = rectangle_length * rectangle_width
area = ((pi * radius**2) / 2)+ triangle_area + rectangle_area
print(area)
