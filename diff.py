# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:47:49 2024

@author: banerm
"""

import numpy as np
import math


def finite_diff(y, h=1.0):
    # Check that the spacing h is positive
    if h <= 0:
        raise ValueError("Spacing h must be positive.")

    # Number of data points
    n = len(y)
    
    # Initialize the array for the derivative
    dydx = np.zeros(n)

    # Forward difference for the first point
    dydx[0] = (y[1] - y[0]) / h

    # Central difference for the interior points
    for i in range(1, n - 1):
        dydx[i] = (y[i + 1] - y[i - 1]) / (2 * h)

    # Backward difference for the last point
    dydx[-1] = (y[-1] - y[-2]) / h

    return dydx

# Example usage (uncomment to test)
# y = np.array([1, 2, 4, 7, 11])
# h = 1.0
# print(finite_diff(y, h))


def fd_formula(x, deriv=1):
    # Check for valid types and values
    if not isinstance(deriv, int):
        raise TypeError("deriv must be an integer.")
    if deriv < 0:
        raise ValueError("deriv must be non-negative.")
    if deriv > len(x) - 1:
        raise ValueError("deriv must be less than or equal to the number of points minus one.")
    
    n = len(x)  # Number of points
    A = np.zeros((deriv + 1, deriv + 1))  # Coefficient matrix
    b = np.zeros(deriv + 1)  # Right-hand side for derivatives

    # Fill the b vector for the derivatives
    for i in range(deriv + 1):
        b[i] = math.factorial(i)  # Factorials for the right-hand side

    # Constructing the matrix A
    for i in range(deriv + 1):
        for j in range(deriv + 1):
            # A[i][j] represents the i-th derivative evaluated at 0 for j-th Taylor expansion
            A[i, j] = (1 / math.factorial(j)) * (i ** j)

    # Solve for coefficients
    c = np.linalg.solve(A, b)

    # For backward difference coefficients, adjust based on the specific method
    if deriv == 1:
        # Backward difference: c[0] = -1, c[1] = 1
        c = np.array([-1, 1]) / (x[1] - x[0])
    elif deriv == 2:
        # Second-order centered difference
        c = np.array([1, -2, 1]) / ((x[1] - x[0]) ** 2)
    elif deriv == 4:
        # Fourth-order centered difference
        c = np.array([-1/12, 2/3, 0, -2/3, 1/12]) / (x[1] - x[0])
    
    return c