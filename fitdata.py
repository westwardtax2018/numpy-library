# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:51:30 2024

@author: banerm
"""
import numpy as np

def back_sub(U, b):
    """
    Solve an upper triangular linear system Ux = b.

    This function takes an upper triangular matrix U and a vector b, and uses back substitution 
    to find the vector x. It returns the solution to the system of equations.

    Parameters:
    U : ndarray
        A square upper triangular matrix.
    b : ndarray
        A 1D array of constants with the same length as the number of columns in U.

    Returns:
    x : ndarray
        A 1D array containing the solution to the linear system.
    """
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    return x

def calc_Vandermonde_matrix(x, d):
    """
    Create a Vandermonde matrix for polynomial fitting.

    This function generates a Vandermonde matrix for the input x data, where each row corresponds 
    to a value of x and each column corresponds to increasing powers of x up to the specified degree d.

    Parameters:
    x : ndarray
        A 1D array of x-coordinates.
    d : int
        The degree of the polynomial fit.

    Returns:
    V : ndarray
        A 2D array representing the Vandermonde matrix.
    """
    n = len(x)
    V = np.ones((n, d + 1))
    for i in range(n):
        for j in range(1, d + 1):
            V[i, j] = x[i] ** j
    return V

def calc_fit(xdata, ydata, degree=1):
    """
    Calculate the coefficients for a polynomial fit using least squares.

    This function fits a polynomial of a specified degree to the provided (x, y) data using 
    the least-squares method. It constructs the Vandermonde matrix and uses QR decomposition 
    to solve for the coefficients.

    Parameters:
    xdata : ndarray
        A 1D array of x-coordinates.
    ydata : ndarray
        A 1D array of y-coordinates.
    degree : int, optional
        The degree of the polynomial fit (default is 1 for linear).

    Returns:
    c : ndarray
        A 1D array of polynomial coefficients [c0, c1, ..., cd].
    """
    V = calc_Vandermonde_matrix(xdata, degree)
    Q, R = np.linalg.qr(V)
    c = back_sub(R, np.dot(Q.T, ydata))
    return c

def eval_fit(c, xfit):
    """
    Evaluate a polynomial at given x-coordinates.

    This function computes the y-values of a polynomial defined by coefficients c at specified 
    x-coordinates. It uses the polynomial equation y = c0 + c1*x + ... + cd*x^d.

    Parameters:
    c : ndarray
        A 1D array of polynomial coefficients [c0, c1, ..., cd].
    xfit : ndarray
        A 1D array of x-coordinates where the polynomial is to be evaluated.

    Returns:
    yfit : ndarray
        A 1D array of computed y-coordinates at each xfit value.
    """
    yfit = np.zeros_like(xfit)
    for i in range(len(c)):
        yfit += c[i] * xfit ** i
    return yfit

    

