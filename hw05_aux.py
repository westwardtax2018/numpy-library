# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:57:34 2024

@author: banerm
"""

import numpy as np

def initialize_T_distribution(num_times, nx, T0, TLBC, TRBC):
    """
    Initialize the temperature distribution array.

    Parameters:
    num_times : int
        The number of time steps for the simulation.
    nx : int
        The number of spatial nodes along the material.
    T0 : float
        The initial temperature of the material at all spatial nodes.
    TLBC : float
        The temperature at the left boundary condition (first node).
    TRBC : float
        The temperature at the right boundary condition (last node).

    Returns:
    ndarray
        A 2D numpy array of shape (num_times, nx) containing the initialized 
        temperature distribution, where the first row corresponds to the initial 
        temperature and the first and last columns correspond to the left and 
        right boundary conditions, respectively.

    Notes:
    This function sets the initial temperature across the spatial domain
    and applies the boundary conditions at the edges.
    """
    T_distribution = np.zeros((num_times, nx))
    T_distribution[0, :] = T0  # Set initial temperature for the first time step
    T_distribution[:, 0] = TLBC  # Set left boundary condition
    T_distribution[:, -1] = TRBC  # Set right boundary condition
    return T_distribution

def solve_PDE(T_old, t_initial, t_final, dt, dx):
    """
    Solve the heat equation using finite difference method.

    Parameters:
    T_old : ndarray
        The temperature distribution from the previous time step.
    t_initial : float
        The initial time of the simulation.
    t_final : float
        The final time of the simulation.
    dt : float
        The time step for the simulation.
    dx : float
        The spatial step size.

    Returns:
    ndarray
        The updated temperature distribution for the next time step.

    Raises:
    ValueError:
        If the stability criterion is violated based on the provided dt and dx.

    Notes:
    This function updates the temperature distribution using the finite 
    difference method and checks for stability based on the thermal diffusivity.
    """
    alpha_val = 1e-5  # Thermal diffusivity value
    
    # Calculate the number of time steps
    n_steps = int((t_final - t_initial) / dt)
    T_new = np.copy(T_old)

    # Check that dt is reasonable based on stability criterion
    if dt >= (dx**2) / (2 * alpha_val):
        raise ValueError(f"Stability criterion violated for dt={dt}, dx={dx}, alpha={alpha_val}")

    # Time-stepping loop
    for step in range(n_steps):
        # Update temperature using finite difference method
        for i in range(1, len(T_old) - 1):
            T_new[i] = T_old[i] + (dt * alpha_val / dx**2) * (T_old[i+1] - 2*T_old[i] + T_old[i-1])
        
        # Update T_old for the next iteration
        T_old = np.copy(T_new)

    return T_new