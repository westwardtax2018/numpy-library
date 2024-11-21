# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:48:11 2024

@author: banerm
"""

import numpy as np

def midpoint(fvals, dx):
    """
    Calculate the midpoint-rule approximation to an integral.

    Parameters:
    fvals (numpy.ndarray): A one-dimensional array of values representing the integrand
                           evaluated at the midpoints of uniformly spaced intervals.
    dx (float): The width of each interval (Δx). Must be positive.

    Returns:
    float: The midpoint-rule approximation to the integral.

    Raises:
    ValueError: If dx is not positive.
    """
    if dx <= 0:
        raise ValueError("dx must be a positive number.")
    
    return np.sum(fvals) * dx

def trapezoidal(fvals, dx):
    """
    Calculate the trapezoidal-rule approximation to an integral.

    Parameters:
    fvals (numpy.ndarray): A one-dimensional array of values representing the integrand
                           evaluated on a uniform grid.
    dx (float): The width of each interval (Δx). Must be positive.

    Returns:
    float: The trapezoidal-rule approximation to the integral.

    Raises:
    ValueError: If dx is not positive.
    """
    if dx <= 0:
        raise ValueError("dx must be a positive number.")
    
    # Trapezoidal rule: (1/2) * (f(a) + f(b)) + Σ f(xi) for i=1 to n-1
    return (dx / 2) * (fvals[0] + 2 * np.sum(fvals[1:-1]) + fvals[-1])

def gauss_quad(func, numpts, a=-1, b=1):
    """
    Estimates the definite integral of a function using Gauss-Legendre quadrature.
    
    This function uses Gauss-Legendre quadrature for 1, 2, or 3 points to approximate
    the integral of a given function `func` over the interval [a, b].
    
    Parameters:
    func (function): The function to integrate. It should take a single argument (x).
    numpts (int): The number of nodes to use in the quadrature (1, 2, or 3).
    a (float): The lower bound of the integration (default is -1).
    b (float): The upper bound of the integration (default is 1).
    
    Returns:
    float: The estimated value of the integral.
    
    Raises:
    ValueError: If numpts is not in [1, 2, 3] or if a > b.
    """
    
    # Validate the inputs
    if a > b:
        raise ValueError("The lower limit a must be less than or equal to the upper limit b.")
    if numpts not in [1, 2, 3]:
        raise ValueError("Only 1, 2, or 3 nodes are supported for Gauss-Legendre quadrature.")
    
    # Gauss-Legendre nodes (xi) and weights (wi) for n = 1, 2, 3
    if numpts == 1:
        xi = [0]
        wi = [2]
    elif numpts == 2:
        xi = [-1/np.sqrt(3), 1/np.sqrt(3)]
        wi = [1, 1]
    elif numpts == 3:
        xi = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
        wi = [5/9, 8/9, 5/9]
    
    # Change of interval: map [a, b] to [-1, 1]
    midpoint = 0.5 * (a + b)
    half_width = 0.5 * (b - a)
    
    # Initialize the result for the integral
    integral = 0.0
    
    # Perform the quadrature summation
    for i in range(numpts):
        # Compute the sample point in the original interval
        x_transformed = midpoint + half_width * xi[i]
        # Compute the weighted function value at the transformed point
        integral += wi[i] * func(x_transformed)
    
    # Multiply by the width of the interval to get the final integral value
    integral *= half_width
    
    return integral