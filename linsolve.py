# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:32:46 2024

@author: banerm
"""


def forward_sub(lu_fac, b):
    """finds the forward substitution
    """
    y = b.copy()
    
    
    for i in range(1, lu_fac.shape[0]):
        for j in range(0, i):
            y[i] -= lu_fac[i,j] * y[j]
            
        
    return y

def back_sub(lu_fac, y):

    
    """
    Perform back substitution to solve the upper triangular system Ux = b.
    
    Parameters:
    U : numpy.ndarray
        Upper triangular matrix of coefficients.
    b : numpy.ndarray
        Right-hand side vector.
    
    Returns:
    x : numpy.ndarray
        Solution vector.
    """
    assert lu_fac.ndim == 2 and lu_fac.shape[0] == lu_fac.shape[1]
    assert lu_fac.shape[0] == y.shape[0]
    assert abs(lu_fac[0, 0]) > 1.0e-15
    x = y.copy()
   
    for i in range(lu_fac.shape[1] - 1, -1, -1):
        assert abs(lu_fac[i, i]) > 1.0e-15
        for j in range(i+1, lu_fac.shape[1]):
            x[i] -= lu_fac[i,j] * x[j]
            
        x[i] = (1/lu_fac[i, i]) * x[i]
        
    return x
    