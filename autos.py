"""Define Automobile superclass and subclasses"""

class Automobile(object):
    """A road vehicle"""

    def __init__(self, name, mpg, fuel_cap):
        """Initialize the name, miles-per-gallon, and fuel capacity."""
        if mpg < 0.0 or fuel_cap < 0.0:
            raise ValueError("MPG and fuel capacity must be positive.")
        self._name = name
        self._mpg = mpg
        self._fuel_cap = fuel_cap

    def __str__(self):
        """Return a string representation of this Automobile."""
        return (self._name + "\n" +
                "\tmpg = " + str(self._mpg) + "\n" +
                "\tfuel capacity = " + str(self._fuel_cap) + "\n")

    def get_mpg(self):
        """Return the Automobile's miles-per-gallon."""
        return self._mpg

    def get_fuel_capacity(self):
        """Return the Automobile's fuel capacity."""
        return self._fuel_cap

    def calc_max_distance(self):
        """Return the maximum distance the Automobile can travel."""
        return self._mpg*self._fuel_cap


class Car(Automobile):
    """A passenger road vehicle"""

    def __init__(self, name, mpg, fuel_cap, convertible=False):
        """Set the name, miles-per-gallon, fuel capacity, and whether or not a convertible."""
        Automobile.__init__(self, name, mpg, fuel_cap)
        self._convertible = convertible

    def __str__(self):
        """Return a string representation of this Car."""
        return (Automobile.__str__(self) +
                "\tconvertible = " + str(self._convertible) + "\n")

    def is_convertible(self):
        """Returns True if this Car is a convertible, False otherwise."""
        return self._convertible


class Truck(Automobile):
    """A heavy road vehicle designed to carry products."""

    def __init__(self, name, mpg, fuel_cap, max_load):
        """Set the name, miles-per-gallon, fuel capacity, and maximum load."""
        Automobile.__init__(self, name, mpg, fuel_cap)
        if max_load < 0.0:
            raise ValueError("Maximum load must be positive.")
        self._max_load = max_load

    def __str__(self):
        """Return a string representation of this Truck."""
        return (Automobile.__str__(self) +
                "\tmaximum load = " + str(self._max_load) + "\n")

    def get_max_load(self):
        """Return the Truck's maximum load."""
        return self._max_load
