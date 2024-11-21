# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:05:27 2024

@author: banerm
"""

import numpy as np
from linsolve import back_sub

def solve_ls(A, b):
    """
    

    Parameters
    ----------
    A : matrix
    b : from Ax = b
    s

    Returns
    -------
    x : back substitution

    """
    q, r = np.linalg.qr(A)
    QT_b = np.dot(q.T, b)
    
    x = back_sub(r, QT_b)
    
    return x
