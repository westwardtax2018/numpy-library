# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:24:09 2024

@author: banerm
"""

# lagrange.py
"""
lagrange.py

This module contains functions for performing Lagrange interpolation.
"""

import numpy as np

def interpolate(xdata, ydata, xeval, tol=1e-12):
    """
    Perform Lagrange interpolation.

    Parameters:
    xdata : array_like
        The x-coordinates of the data points.
    ydata : array_like
        The y-coordinates of the data points.
    xeval : array_like
        The x-coordinates where interpolation is to be performed.

    Returns:
    result : ndarray
        The interpolated values at the specified x-coordinates.

    Raises:
    ValueError: If input arrays have different sizes or if less than two points are provided.
    ZeroDivisionError: If the denominator in the Lagrange basis polynomial is too small.
    """
    
    if len(xdata) != len(ydata):
        raise ValueError("Input arrays must have the same length.")
    
    if len(xdata) < 2:
        raise ValueError("At least two data points are required for interpolation.")
    
    # Check for non-unique x data within the specified tolerance
    for i in range(len(xdata)):
        for j in range(i + 1, len(xdata)):
            if abs(xdata[i] - xdata[j]) < tol:
                raise ZeroDivisionError("Non-unique x data found within tolerance.")

    # Initialize result
    result = np.zeros_like(xeval)
    
    for j, x in enumerate(xeval):
        total = 0.0
        for i in range(len(xdata)):
            # Compute the Lagrange basis polynomial L_i
            L_i = 1.0
            for m in range(len(xdata)):
                if m != i:
                    L_i *= (x - xdata[m]) / (xdata[i] - xdata[m])
            total += L_i * ydata[i]
        result[j] = total
    
    return result


    



