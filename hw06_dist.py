# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:37:48 2024

@author: banerm
"""
import numpy as np


def uniform(xlo, xhi):
    """
    Generate a uniformly distributed random number between xlo and xhi.
    
    Parameters:
    - xlo: float, lower bound of the distribution.
    - xhi: float, upper bound of the distribution.
    
    Returns:
    - A float uniformly distributed in the interval [xlo, xhi).
    
    Raises:
    - ValueError: if xlo >= xhi.
    """
    if xlo >= xhi:
        raise ValueError("xlo must be less than xhi")
    return xlo + (xhi - xlo) * np.random.random()

def normal(mu, sigma, low, high):
    """
    Generate a random number from a truncated normal distribution.
    
    Parameters:
    - mu: float, mean of the normal distribution.
    - sigma: float, standard deviation of the normal distribution.
    - low: float, lower bound for truncation.
    - high: float, upper bound for truncation.
    
    Returns:
    - A float drawn from the truncated normal distribution.
    
    Raises:
    - ValueError: if low >= high or if sigma <= 0.
    """
    if low >= high:
        raise ValueError("low must be less than high")
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    
    # Repeatedly sample until the value is within the bounds
    while True:
        sample = np.random.normal(mu, sigma)
        if low <= sample <= high:
            return sample
        
def dirac(x):
    """
    Return a constant value, representing a Dirac distribution.
    
    Parameters:
    - x: float, the constant value.
    
    Returns:
    - x: float.
    """
    return x



