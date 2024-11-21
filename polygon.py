"""A module for the geometry of polygons"""

from math import sqrt

class Polygon(object):
    """An abstract base class for plane figures with at least 3 sides"""
    _num_sides = 0

    def __init__(self, height, width):
        """initialize a polygon of `height` and `width` dimensions"""
        if height < 0.0 or width < 0.0:
            raise ValueError("height and width must be positive.")
        self._h = height
        self._w = width

    def get_num_sides(self):
        """returns the number of sides the polygon has"""
        return self._num_sides

    def calc_area_perimeter_ratio(self):
        """returns the ratio of the polygon's area to its perimeter"""
        return self.calc_area()/self.calc_perimeter()
class RightTriangle(Polygon):
    """A class to represent a right triangle."""
    
    _num_sides = 3  # Right triangle has 3 sides

    def __init__(self, height, width):
        """Initialize a RightTriangle instance with given height and width."""
        super().__init__(height, width)  # Call the base class constructor

    def calc_area(self):
        """Calculate and return the area of the right triangle."""
        return 0.5 * self._h * self._w

    def calc_perimeter(self):
        """Calculate and return the perimeter of the right triangle."""
        hypotenuse = (self._h ** 2 + self._w ** 2) ** 0.5
        return self._h + self._w + hypotenuse


class Rectangle(Polygon):
    """A class to represent a rectangle."""
    
    _num_sides = 4  # Rectangle has 4 sides

    def __init__(self, height, width):
        """Initialize a Rectangle instance with given height and width."""
        super().__init__(height, width)  # Call the base class constructor

    def calc_area(self):
        """Calculate and return the area of the rectangle."""
        return self._h * self._w

    def calc_perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self._h + self._w)
