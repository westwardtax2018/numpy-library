# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:42:46 2024

@author: banerm
"""

from specifications import P, theta, d, h, L 
from math import sin, cos, tan, pi

Px = -P*cos((90 - theta)*(pi/180))
Py = P*sin((90 - theta)*(pi/180))

F = -Px

R = (L*P) / d

N = R - Py

rho = L / d

    
