# -*- coding: utf-8 -*-
"""
hw05.py

This module contains functions for solving the heat equation using finite difference methods 
and for performing Lagrange interpolation.
"""

import numpy as np
import hw05_aux
import matplotlib.pyplot as plt  # Ensure this library is installed

# Constants
L = 0.01  # Length of the material (meters)
T0 = 20.0  # Initial temperature (°C)
TLBC = 170.0  # Left boundary condition temperature (°C)
TRBC = 20.0  # Right boundary condition temperature (°C)
dt = 0.01  # Time step
nx = 20  # Number of spatial nodes

# Define spatial discretization
dx = L / (nx - 1)
x = np.linspace(0, L, nx)

# Time array
times = np.array([0.0, 0.1, 0.3, 1.0, 3.0, 10.0])

# Initialize temperature distribution
T_distribution = hw05_aux.initialize_T_distribution(len(times), nx, T0, TLBC, TRBC)

# Loop to compute temperature distributions at specified times
for i in range(1, len(times)):
    T_distribution[i] = hw05_aux.solve_PDE(T_distribution[i-1], times[i-1], times[i], dt, dx)

# Plotting the results
plt.figure()
for i in range(len(times)):
    plt.plot(x, T_distribution[i], label=f"t = {times[i]} s")
plt.title("Temperature Distribution in Material Over Time")
plt.xlabel("Position (m)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.xlim([-0.03 * L, 1.03 * L])
plt.ylim([0, max(TLBC, T0) + 10])  # Add some padding
plt.grid()
plt.savefig("hw05plot.png")
plt.show()