# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:25:08 2024

@author: banerm
"""

# 1. dy/dt = -0.01y
A1 = 200  # Maximum stable time step

# 2. 0.2 dp/dt = -36p -> dp/dt = -180p
A2 = 1 / 90  # Maximum stable time step

# 3. dm/dt = (-0.75 + i1.2)m
A3 = 0.7490636704119851    # Maximum stable time step

# 4. 0.5 dw/dt = -i√2w
A4 = 0  # No stable time step for purely imaginary eigenvalue

