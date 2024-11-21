# Solution to Homework Assignment 02

from hw02_aux import dot_product, cross_product, normalize_vector
from hw02_inp import F, tx, ty, tz, b, c, Dx, Dy, Dz

import numpy as np
# note that you can use function np.cos
# and value np.pi, etc.

# Write your code below here

if F < 1.0e-8:
    F_O = np.array([0.0, 0.0, 0.0])
    M_O = np.array([0.0, 0.0, 0.0])
    M_OD = np.array([0.0, 0.0, 0.0])
else:
    F_O = np.array([F*np.cos(tx*(np.pi/180)),F*np.cos(ty*(np.pi/180)),F*np.cos(tz*(np.pi/180))])

    r_OA = np.array([b,c,0])
    M_O = cross_product(r_OA, F_O)

    if Dx < 1.0e-10 and Dy < 1.0e-10 and Dz < 1.0e-10:
        M_OD = np.array([0.0, 0.0, 0.0])
        
    else:
        D = np.array([Dx,Dy,Dz])
        e_OD = normalize_vector(D)
        M_OD = (dot_product(M_O, e_OD))*e_OD

    

print("F_O  = ", F_O )
print("M_O  = ", M_O )
print("M_OD = ", M_OD)
