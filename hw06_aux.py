import numpy as np


"""Auxiliary functions for hw06 LSC simulation"""



def vector_magnitude(v):
    """
    Calculate the magnitude of a vector.
    
    Parameters:
    - v: ndarray, the 2D vector.
    
    Returns:
    - float, the magnitude of the vector.
    """
    return np.sqrt(np.sum(v**2))
    


def scale_ray(ray, magnitude):
    """
    Scale a given ray to a new magnitude.
    
    Parameters:
    - ray: ndarray, the input ray with two points (p0, p1).
    - magnitude: float, the new magnitude of the ray.
    
    Returns:
    - A new ray with the same direction but the specified magnitude.
    """
    # Ensure ray is a 2D array with shape (2, 2)
    if ray.ndim != 2 or ray.shape[0] != 2 or ray.shape[1] != 2:
        raise ValueError("Input 'ray' must be a 2D array with shape (2, 2)")

    # Compute ray vector (p1 - p0)
    ray_vector = ray[1, :] - ray[0, :]
    
    # Compute the unit vector
    unit_vector = ray_vector / np.linalg.norm(ray_vector)
    
    # Scale the unit vector by the magnitude
    scaled_vector = unit_vector * magnitude
    
    # Compute the new p1 position
    new_p1 = ray[0, :] + scaled_vector
    
    # Return the new scaled ray
    return np.array([ray[0, :], new_p1])
    


def rotate_vector(u, theta):
    """
    Rotate a 2D vector u by an angle theta (in degrees).
    
    Parameters:
    - u: ndarray, the vector to rotate.
    - theta: float, the angle in degrees to rotate anticlockwise.
    
    Returns:
    - ndarray, the rotated vector.
    """
    # Convert angle to radians
    theta_rad = np.deg2rad(theta)
    
    # Rotation matrix
    rotation_matrix = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                                [np.sin(theta_rad), np.cos(theta_rad)]])
    
    # Rotate the vector
    rotated_vector = np.dot(rotation_matrix, u)
    
    return rotated_vector


def perpendicular_vector(ln, pt, iopt = 0):
    """Compute vector between point and line perpendicular to line.
    
    `ln` is a 2D ndarray [ [x0,y0], [x1,y1] ] storing the
         start and end (x, y) coordinates of a surface.
    `pt` is a 1D ndarray [x,y] storing the (x,y) coordinates
         of a point

    Uses the vector and dot product method.
        u is the vector along the line
        v is the vector from first vertex and given point
        a is the projected vector along the line
        b is the perpendicular vector
        iopt = 0: vector from point to line
             = 1: vector from line to point
    """
    import numpy as np
    u = ln[1,:] - ln[0,:]
    u2 = np.dot(u, u)
    v = pt[:] - ln[0,:]
    dp = np.dot(u, v)
    a = dp * u / u2
    if(iopt == 0):
        b = a - v
    else:
        b = v - a
    return b


def get_new_location(location, angle, shoot):
    """Compute transported ray location point after interaction.
    
    INPUT:  location - 1D ndarray float current (x, y) location of the ray
            angle    - angle of ray with respect to x axis, in degrees
            shoot    - distance the ray moves
    OUTPUT: newloc   - 1D ndarray float new (x, y) location of the ray
    """
    import numpy as np
    rangle = (180.0 + angle) * np.pi/180.0
    dx = np.cos(rangle) * shoot
    dy = np.sin(rangle) * shoot
    dp = np.array([dx, dy])
    newloc = location + dp
    return newloc


def intersection(l1, l2):
    """Point of intersection of line segments `l1` and `l2`.
    
    INPUT:  l1, l2 - 2D ndarrays [ [x0,y0], [x1,y1] ] storing the
                     start and end (x, y) coordinates of the lines
    OUTPUT: inters - Boolean; True if there is an intersection, and
                              False if they don't intersect
            xpt    - (x, y) coordinate of point of intersection
    """
    import numpy as np

    d1 = perpendicular_vector(l1, l2[0,:], 1)
    d2 = perpendicular_vector(l1, l2[1,:], 1)
    dp = np.dot(d1, d2)
    
    # find the fraction at intersection
    d1lensq = np.dot(d1, d1)
    d2lensq = np.dot(d2, d2)
    d1len = np.sqrt(d1lensq)
    d2len = np.sqrt(d2lensq)

    #interpolate the value to find the intersection
    # x -> 0 , 1; y -> a, b; y=0 gives x = a/(a-b)
    frac = d1len / (d1len - np.sign(dp) * d2len)
    
    xpt = l2[0,:] + frac *(l2[1,:] - l2[0,:])
    
    inters = True
    if(frac < 0.0 or frac > 1.0):
        inters = False

    return inters, xpt
