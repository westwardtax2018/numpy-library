# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:00:56 2024

@author: banerm
"""
"""
hw05_alpha.py

This module contains functions for reading data and calculating thermal
diffusivity for heat transfer problems.
"""

import numpy as np
from lagrange import interpolate

def read_data(filename):
    """
    Read temperature and diffusivity data from a CSV file.

    Parameters:
    filename : str
        The path to the CSV file containing temperature and diffusivity data.

    Returns:
    temperatures : ndarray
        Array of temperature values.
    diffusivities : ndarray
        Array of diffusivity values.

    Raises:
    FileNotFoundError: If the file does not exist.
    ValueError: If the data format is incorrect.
    """
    data = np.loadtxt(filename, skiprows=6, delimiter=",", usecols=(0, 3))
    temperatures = data[:, 0]  # Change this line if necessary
    diffusivities = data[:, 1]  # Adjust this line as well

    # Assertions to validate data
    assert temperatures[0] == 0.0, "First temperature should be 0.0"
    assert temperatures[-1] == 1000.0, "Last temperature should be 1000.0"
    assert np.all(diffusivities < 1.0e-5), "All diffusivities should be less than 1.0e-5"

    return temperatures, diffusivities

# Set module variables
filename = 'ss304_thermal_diffusivity_data.csv'
temperatures, diffusivities = read_data(filename)

def alpha(T):
    """
    Return the thermal diffusivity for a given temperature.

    Parameters:
    T : float
        The temperature at which to calculate the thermal diffusivity.

    Returns:
    float
        The calculated thermal diffusivity at the given temperature.

    Raises:
    TypeError: If T is not a scalar.
    ValueError: If T is outside the range [0.0, 1000.0] degrees Celsius.
    """
    if np.ndim(T) != 0:
        raise TypeError("Input must be a scalar.")

    if not (0.0 <= T <= 1000.0):
        raise ValueError("Temperature must be between 0.0 and 1000.0 degrees Celsius.")
        
    # Convert T to an array for interpolation
    return interpolate(temperatures, diffusivities, np.array([T]))[0]  # Return a scalar
