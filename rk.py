# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 01:34:12 2024

@author: banerm
"""

import numpy as np

def explicit_midpoint(func, tspan, y0, num_steps):
    """
    Solves an initial value problem (IVP) using the Explicit Midpoint Scheme (a 2nd-order Runge-Kutta method).
    
    Parameters:
    -----------
    func : function
        The function F(y,t) that defines the differential equation dy/dt = F(y,t).
        It should take in the arguments y (the current solution) and t (the current time).
    
    tspan : array_like
        A list or array with two elements representing the start and end times [t0, tf].
        
    y0 : float
        The initial condition, y(t0), at time t0.
        
    num_steps : int
        The number of time steps to be used in the integration.
        
    Returns:
    --------
    t : ndarray
        An array of time points from t0 to tf, inclusive.
        
    y : ndarray
        An array of solution values corresponding to each time point in t.
        
    Raises:
    -------
    ValueError : If tspan[0] > tspan[1] or num_steps < 1.
    """
    # Validate inputs
    if tspan[0] > tspan[1]:
        raise ValueError("tspan[0] must be less than or equal to tspan[1]")
    if num_steps < 1:
        raise ValueError("num_steps must be at least 1")

    # Initialize variables
    t0, tf = tspan
    h = (tf - t0) / num_steps  # Step size
    t = np.linspace(t0, tf, num_steps + 1)  # Time array
    y = np.zeros(num_steps + 1)  # Solution array
    y[0] = y0  # Initial condition

    # Explicit midpoint scheme
    for n in range(num_steps):
        tn = t[n]
        yn = y[n]

        # Midpoint approximation
        k1 = func(yn, tn)  # Slope at the current point
        k2 = func(yn + 0.5 * h * k1, tn + 0.5 * h)  # Slope at the midpoint
        
        # Update the solution using the midpoint formula
        y[n+1] = yn + h * k2
    
    return t, y


def runge_kutta_4th(func, tspan, y0, num_steps):
    """
    Solves an initial value problem (IVP) using the Classical 4th-Order Runge-Kutta Scheme.
    
    Parameters:
    -----------
    func : function
        The function F(y,t) that defines the differential equation dy/dt = F(y,t).
        It should take in the arguments y (the current solution) and t (the current time).
    
    tspan : array_like
        A list or array with two elements representing the start and end times [t0, tf].
        
    y0 : float
        The initial condition, y(t0), at time t0.
        
    num_steps : int
        The number of time steps to be used in the integration.
        
    Returns:
    --------
    t : ndarray
        An array of time points from t0 to tf, inclusive.
        
    y : ndarray
        An array of solution values corresponding to each time point in t.
        
    Raises:
    -------
    ValueError : If tspan[0] > tspan[1] or num_steps < 1.
    """
    # Validate inputs
    if tspan[0] > tspan[1]:
        raise ValueError("tspan[0] must be less than or equal to tspan[1]")
    if num_steps < 1:
        raise ValueError("num_steps must be at least 1")

    # Initialize variables
    t0, tf = tspan
    h = (tf - t0) / num_steps  # Step size
    t = np.linspace(t0, tf, num_steps + 1)  # Time array
    y = np.zeros(num_steps + 1)  # Solution array
    y[0] = y0  # Initial condition

    # Classical 4th-order Runge-Kutta scheme
    for n in range(num_steps):
        tn = t[n]
        yn = y[n]

        # Compute the 4 slopes (k1, k2, k3, k4)
        k1 = func(yn, tn)
        k2 = func(yn + 0.5 * h * k1, tn + 0.5 * h)
        k3 = func(yn + 0.5 * h * k2, tn + 0.5 * h)
        k4 = func(yn + h * k3, tn + h)

        # Update the solution using the RK4 formula
        y[n+1] = yn + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
    
    return t, y