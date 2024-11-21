# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:59:35 2024

@author: banerm
"""

import numpy as np

def forward_euler(func, tspan, y0, num_steps):
    """
    Solve a scalar initial value problem (IVP) using the forward Euler method.

    Parameters:
    - func: A function representing F(y,t) where y is the dependent variable
            and t is the independent variable.
    - tspan: A list or array with two elements [t0, tf] representing the start
             and end time.
    - y0: The initial condition at t0.
    - num_steps: The number of time steps to take from t0 to tf.

    Returns:
    - t: A numpy array of time points [t0, t1, ..., tf].
    - y: A numpy array of the corresponding solution at each time point.

    Raises:
    - ValueError: If tspan[0] > tspan[1] or num_steps < 1.
    """
    # Validate input
    if tspan[0] > tspan[1]:
        raise ValueError("The start time t0 must be less than or equal to the end time tf.")
    if num_steps < 1:
        raise ValueError("The number of steps must be at least 1.")

    # Initialize time array and solution array
    t0, tf = tspan
    dt = (tf - t0) / num_steps  # time step size
    t = np.linspace(t0, tf, num_steps + 1)  # array of time points
    y = np.zeros(num_steps + 1)  # array to store solutions
    y[0] = y0  # set the initial condition

    # Perform the forward Euler method
    for n in range(num_steps):
        y[n + 1] = y[n] + dt * func(y[n], t[n])

    return t, y


from scipy.optimize import root_scalar

def backward_euler(func, tspan, y0, num_steps):
    """
    Solve a scalar initial value problem (IVP) using the backward Euler method.

    Parameters:
    - func: A function representing F(y,t) where y is the dependent variable
            and t is the independent variable.
    - tspan: A list or array with two elements [t0, tf] representing the start
             and end time.
    - y0: The initial condition at t0.
    - num_steps: The number of time steps to take from t0 to tf.

    Returns:
    - t: A numpy array of time points [t0, t1, ..., tf].
    - y: A numpy array of the corresponding solution at each time point.

    Raises:
    - ValueError: If tspan[0] > tspan[1] or num_steps < 1.
    """
    # Validate input
    if tspan[0] > tspan[1]:
        raise ValueError("The start time t0 must be less than or equal to the end time tf.")
    if num_steps < 1:
        raise ValueError("The number of steps must be at least 1.")

    # Initialize time array and solution array
    t0, tf = tspan
    dt = (tf - t0) / num_steps  # time step size
    t = np.linspace(t0, tf, num_steps + 1)  # array of time points
    y = np.zeros(num_steps + 1)  # array to store solutions
    y[0] = y0  # set the initial condition

    # Perform the backward Euler method
    for n in range(num_steps):
        # Function for root finding: g(y_{n+1}) = y_{n+1} - y_n - dt * F(y_{n+1}, t_{n+1})
        def g(y_next):
            return y_next - y[n] - dt * func(y_next, t[n+1])

        # Solve the root-finding problem using secant method
        # Initial guesses: y[n] (previous value) and y[n] + dt * func(y[n], t[n])
        sol = root_scalar(g, method='secant', x0=y[n], x1=y[n] + dt * func(y[n], t[n]))

        # Check if the solver converged successfully
        if sol.flag != 0:
            raise RuntimeError(f"Root-finding failed at step {n+1}. Solver flag: {sol.flag}")
        
        y[n+1] = sol.root

    return t, y