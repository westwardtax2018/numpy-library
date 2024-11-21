# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:36:50 2024

@author: banerm
"""

import numpy as np


# =============================================================================
# INTERACTIONS FOR RAYS WITH SURFACES
# =============================================================================

def glass_interaction(surf, ray, crit_angle):
    """Handle the interaction of a ray with a glass surface (top surface).
    
    Parameters:
    surf - The surface that the ray interacts with.
    ray  - The current ray (an array with 2 points: start and end).
    crit_angle - The critical angle for total internal reflection.
    
    Returns:
    refln - Boolean, True if the ray is reflected, False if it exits the LSC.
    nray  - The new ray direction after interaction.
    """
    p0, p1 = ray
    normal = get_surface_normal(surf)
    
    # Calculate the incident angle (relative to normal)
    incident_angle = angle_between_vectors(p1 - p0, normal)
    
    if incident_angle > crit_angle:
        # Total internal reflection (refract)
        refln = True
        nray = reflect_ray(p1, normal)
    else:
        # Ray exits LSC
        refln = False
        nray = p1  # ray leaves, so no change in direction
        
    return refln, nray


def mirror_interaction(surf, ray):
    """Handle interaction of a ray with a mirror (reflecting surface).
    
    Parameters:
    surf - The surface that the ray interacts with.
    ray  - The current ray (an array with 2 points: start and end).
    
    Returns:
    nray - The new ray direction after interaction.
    """
    # Ensure ray is a 2D array with shape (2, 2)
    if ray.shape != (2, 2):
        raise ValueError("Input 'ray' must be a 2D array with shape (2, 2)")
    
    p0, p1 = ray  # Unpack the ray points
    normal = get_surface_normal(surf)  # Get normal vector for the mirror surface
    
    # Reflect the ray
    nray = reflect_ray(p1, normal)  # Reflect the ray based on the normal
    
    return nray


def scatter_interaction(surf, ray):
    """Handle interaction of a ray with a scattering surface (bottom surface).
    
    Parameters:
    surf - The surface that the ray interacts with.
    ray  - The current ray (an array with 2 points: start and end).
    
    Returns:
    nray - The new ray direction after scattering.
    """
    p0, p1 = ray
    
    # Scattering is modeled as a random direction change
    scatter_angle = np.random.uniform(0, 360)  # Random scatter angle
    scatter_direction = np.array([np.cos(np.radians(scatter_angle)), np.sin(np.radians(scatter_angle))])
    
    # Scale the ray in a random direction
    nray = p1 + scatter_direction * np.linalg.norm(p1 - p0)
    
    return nray


def reflect_ray(p1, normal):
    """Reflect the ray from a given point and surface normal."""
    # Reflect ray based on surface normal using reflection formula
    # r = d - 2 * (d . n) * n
    direction = p1 - np.array([0, 0])  # Assuming p1 is the point of incidence
    dot_product = np.dot(direction, normal)
    reflection = direction - 2 * dot_product * normal
    return reflection


def get_surface_normal(surf):
    """Return the surface normal vector given a surface."""
    # Calculate the normal vector of the surface
    p0, p1 = surf
    surface_vector = p1 - p0
    normal = np.array([-surface_vector[1], surface_vector[0]])  # Rotate 90 degrees for normal
    normal = normal / np.linalg.norm(normal)  # Normalize the vector
    return normal


def angle_between_vectors(v1, v2):
    """Calculate the angle between two vectors."""
    dot_product = np.dot(v1, v2)
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)
    cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
    angle = np.degrees(np.arccos(np.clip(cos_theta, -1.0, 1.0)))  # Ensure it is within valid range
    return angle