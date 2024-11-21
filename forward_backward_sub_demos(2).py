"""Script to test forward_sub and back_sub."""

import numpy as np

debug_back_sub = True # set to True to test back_sub

# first test forward sub
from linsolve import forward_sub    
L = np.array([[1., 0., 0.], [2., 1., 0.], [3., 4., 1.]])
b = np.array([1.0, 1.0, 1.0])
y = forward_sub(L, b)

# check that answer is actually a solution
# if L y = b, then Ly - b = 0 <--- zeros array
print( L @ y - b )

if debug_back_sub:
    from linsolve import back_sub

    U = np.array([[1., 2., 3.], [0., 4., 5.], [0., 0., 6.]])
    x = back_sub(U, y)

    # check that answer is actually a solution
    # if U x = y, then Ux - y = 0 <--- zeros array
    print( U @ x - y )
