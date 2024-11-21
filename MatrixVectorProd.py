# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:00:17 2024

@author: banerm
"""

import numpy as np

A = np.load("matrix.npy")
x = np.load("vector.npy")
y = np.zeros(A.shape[0])
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        y[i] += A[i,j] * x[j]
        
np.save("result.npy", y)
