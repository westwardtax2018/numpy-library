# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:53:08 2024

@author: banerm
"""

import random

def estimate_area(func, xlo, xhi, ylo, yhi, n=100):
    """
    Estimates the area inside a 2D curve defined by the function `func`.
    
    The function uses the Monte Carlo simulation method to estimate the area
    under the curve defined by `func(x, y) < 0.0` within the specified bounding
    rectangle defined by `xlo`, `xhi`, `ylo`, and `yhi`.
    
    Parameters:
    func (function): The function that defines the curve. It should take two arguments (x, y).
    xlo (float): The lower bound of x-coordinate.
    xhi (float): The upper bound of x-coordinate.
    ylo (float): The lower bound of y-coordinate.
    yhi (float): The upper bound of y-coordinate.
    n (int): The number of random points to sample (default is 100).
    
    Returns:
    float: The estimated area inside the curve.
    
    Raises:
    ValueError: If `n` is not positive or if `xlo >= xhi` or `ylo >= yhi`.
    """
    
    # Validate input parameters
    if n <= 0:
        raise ValueError("Number of samples n must be positive.")
    if xlo >= xhi:
        raise ValueError("xlo must be less than xhi.")
    if ylo >= yhi:
        raise ValueError("ylo must be less than yhi.")
    
    # Initialize count of points inside the curve
    inside_count = 0
    
    # Perform Monte Carlo sampling
    for _ in range(n):
        # Generate random (x, y) point within the bounds
        x = random.uniform(xlo, xhi)
        y = random.uniform(ylo, yhi)
        
        # Check if the point is inside the curve (i.e., func(x, y) < 0)
        if func(x, y) < 0.0:
            inside_count += 1
    
    # Calculate the area of the bounding box
    area_box = (xhi - xlo) * (yhi - ylo)
    
    # Estimate the area inside the curve
    area_estimate = (inside_count / n) * area_box
    
    return area_estimate