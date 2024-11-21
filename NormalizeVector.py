# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:40:24 2024

@author: banerm
"""

import numpy as np


u = np.array([0.5, -0.6, 1.3])
dot = 0.0
for i in range(u.size):
    dot += u[i]*u[i]
    
u /= dot**(1/2)

print(u)
