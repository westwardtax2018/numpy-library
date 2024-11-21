# Auxiliary functions to use in hw02.py
import numpy as np

def dot_product(u, v):
    """Compute vector dot product:  dot = u . v
    
    This works for NumPy vectors u and v of any size
    but does not verify that u and v are of the same
    size.  The output is the scalar dot product, `dot`.
    
    Requirements:
     - you may not assume that vectors u and v have
       only 3 elements each; this function must work
       for vectors of any size as long as u and v are
       of the same size.
     - you must use a loop to compute the dot product;
       you may not use an imported function to do it
     - the result must be stored in variable `dot`
     - keep the "def" statement above and the "return"
       statement below exactly as they are.
     - be sure that your code starts with four spaces
       of indentation.
    
    """
    # Start your code below here
    
    dot = 0.0
    
    if len(u) == len(v):
        for i in range(len(u)):
            dot += u[i] * v[i]
    else:
        pass
    return dot

def cross_product(u, v):
    """Compute 3D vector cross product:  cross = u x v.
    
    The input u and v must be 3-element 1D Numpy
    arrays.  The output "cross" is similarly a 3-
    element 1D Numpy array per the definition of
    the cross product (but mathematically is
    actually a pseudo-vector).

    Requirements:
     - you must assume that vectors u and v have
       only 3 elements each, as the cross product
       is only defined in 3D.
     - you do not need to use a loop to compute the
       cross product; however, you may still not use
       an imported function to do it either.
     - the result must be stored in variable `cross`
     - keep the "def" statement above and the "return"
       statement below exactly as they are.
     - be sure that your code starts with four spaces
       of indentation.
     - 
    """
    # Start your code below here
    cross = np.array([0.0, 0.0, 0.0])

    cross[0] = u[1]*v[2] - u[2]*v[1]
    cross[1] = -(u[0]*v[2] - u[2]*v[0])
    cross[2] = u[0]*v[1] - u[1]*v[0]
    
    return cross

def normalize_vector(u):
    """Compute normalized vector:  u_hat = u / ||u||.
    
    This uses the dot product formula to compute
    the norm of input Numpy vector `u` and then
    scales u by the norm of u to output `u_hat`.
    
    Recall that the norm of a vector is the square
    root of the dot product of the vector with itself.

    Requirements:
     - you may not assume that vector u has only 3
       elements; this function must work for vectors
       of any size.
     - you must use the dot_product function you wrote
       above to compute u_hat.  See the assignment
       instructions for more details.
     - the result must be stored in variable `u_hat`
     - keep the "def" statement above and the "return"
       statement below exactly as they are.
     - be sure that your code starts with four spaces
       of indentation.
     - 
    """
    # Start your code below here
    u_hat = np.zeros(len(u))
    
    u_mag = dot_product(u, u) ** (1/2)
    
    for i in range(len(u)):
        u_hat[i] = u[i] / u_mag

    return u_hat

