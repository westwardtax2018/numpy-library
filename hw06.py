"""hw06 LSC Simulator"""

import numpy as np
import hw06_dist as dist
import hw06_aux  as aux
import hw06_intr as intr

# =============================================================================
# SIMULATION INITIALIZATION
# =============================================================================
Make_Plot = True
Ray_Text  = False
Debug     = False

# First simulation count (for 10 simulations)
n_sims_10 = 10
# Second simulation count (for 1000 simulations)
n_sims_1000 = 1000

max_interactions = 30
# =============================================================================
# LSC GEOMETRY
# =============================================================================
LENGTH = 1.0 # inches
HEIGHT = 0.1 # inches

# rectangular bounding coordinates of surfaces
#   draw surface from (x0, y0) to (x1, y1)
# -- surface -------------   x0      y0        x1      y1
bottom_surface  = np.array([[0.0   , 0.0   ], [LENGTH, 0.0   ]])
right_surface   = np.array([[LENGTH, 0.0   ], [LENGTH, HEIGHT]])
top_surface     = np.array([[LENGTH, HEIGHT], [0.0   , HEIGHT]])
left_surface    = np.array([[0.0   , HEIGHT], [0.0   , 0.0   ]])

surfaces = np.array([bottom_surface, right_surface, top_surface, left_surface])
nsurfaces = surfaces.shape[0]

type_surf = np.array([2, 3, 0, 1], dtype = int)
type_surf_text = ["top glass", "left mirror",
                  "bottom scatterer", "right PV cell"]
# 0 - glass (top surface)
# 1 - mirror (left surface)
# 2 - scattering surface (bottom surface)
# 3 - PV surface

if Debug:
    print("Number of surfaces =", nsurfaces)
    print()
    print("Surfaces =")
    for s in range(0, nsurfaces):
        print(type_surf_text[s])
        print(surfaces[type_surf[s]])
    print()

solar_angle      = -15.0     # degrees from vertical (CCW is positive)
refraction_angle =  9.80675  # air to glass refraction from Snell's law

max_shoot   =   1.2 * LENGTH
crit_angle  =  42.0          # degrees

# =============================================================================
# INITIATE SIMULATION AND PLOT
# =============================================================================

def plot_surfaces(surfaces):
    """Sequentially plot surfaces of LSC.
    
    INPUT:  surfaces - 3D ndarray of surfaces to plot sequentially,
                       where each element of the array is itself a
                       2D ndarray of coordinate pairs (x0, y0) and
                       (x1, y1) each stored as a 1D ndarray:
    surfaces = [ [[x0, y0], [x1, y1]], [[x0, y0], [x1, y1]],... ]
    
    OUTPUT:  None
    """
    import matplotlib.pyplot as plt
    nsurfaces = surfaces.shape[0]
    for isurf in range(nsurfaces):
        surf = surfaces[isurf, :, :]
        plt.plot(surf[:, 0], surf[:, 1], "b-o")
    return None

if Make_Plot:
    import matplotlib.pyplot as plt
    plt.figure()
    plot_surfaces(surfaces)  # plot LSC surfaces
    plt.axis('equal')        # set equal scaling (i.e., make circles circular)

pv_count = 0
for itr in range(n_sims_10):

    # Start ray into top surface at solar angle and
    #   at random incident location
    iangle = dist.dirac(solar_angle)
    incd_angle = iangle + 90. # convert to angle from x-axis
    incd_location = dist.uniform(0., LENGTH)
    p0 = np.array([incd_location, HEIGHT])   # point on top surface
    if (Debug):
        print("p0 = ", p0)

    # Refract ray at air to glass interface
    if(iangle < 0.0):
        current_angle = incd_angle + refraction_angle
    else:
        current_angle = incd_angle - refraction_angle

    # ray is now in glass surface
    current_surface = 2
    
    p1 = aux.get_new_location(p0, current_angle, max_shoot)
    if (Debug):
        print("p1 = ", p1)
    
    ray = np.array([p0, p1]) # bundle projected trajectory
    
    if (Debug):
        print(" original ray = \n", ray)

    ray_alive = True
    ninteract = 0
    while(ray_alive and ninteract < max_interactions):
        
        if (Ray_Text):
            print("\n interactions :", ninteract)
        
        interact_status = False
        for isurf in range(nsurfaces):
            
            if (Debug):
                print("surface :", isurf)

            if(isurf == current_surface):
                if (Debug):
                    print("skipping current surface")
                continue
                        
            surf = surfaces[isurf, :, :]
            
            ix, xpt = aux.intersection(ray, surf)
            
            if(ix == False):
                if (Debug):
                    print("intersection not inside")
                continue
            
            if (Debug):
                print("interaction in surface", isurf)
            interact_status = True
            current_surface = isurf
            
            ray[1, :] = xpt[:] #update array
            if(Make_Plot == True):
                plt.plot(ray[:, 0], ray[:, 1], "g--o")
            
            if (Debug):
                print("type = ", type_surf[isurf])

            if (type_surf[isurf] == 0):   
                refln, nray = intr.glass_interaction(surf, ray, crit_angle)
                ray_alive = refln
                if(not refln):
                    if Ray_Text:
                        print("ray leaving LSC")
                    dray = ray[:,1]-ray[:,0]
                    ray = aux.scale_ray(nray, 4.0 * HEIGHT)
                if(Make_Plot == True):
                    plt.plot(ray[:, 0], ray[:, 1], "y-.")

            elif (type_surf[isurf] == 1):
                nray = intr.mirror_interaction(surf, ray)
                ray_alive = True

            elif(type_surf[isurf] == 2):
                nray = intr.scatter_interaction(surf, ray)
                ray_alive = True

            else:
                pv_count += 1
                if Ray_Text:
                    print("ray hitting PV")
                ray_alive = False
                break

            if Debug:            
                print("nray = \n", nray)           
            ray = aux.scale_ray(nray, max_shoot)
            
            break # interaction found so go for next itertaion
            
        if Debug:            
            print("ray alive status", ray_alive)
        
        ninteract += 1

efficiency = pv_count / n_sims_10
if Ray_Text:
    print("\nefficiency = ", efficiency)

if Make_Plot:
    import matplotlib.pyplot as plt
    plt.title("Efficiency of LSC by Monte Carlo Simulation (banerm)")
    text_string = "Number of iterations = " + str(n_sims_10) + "\n"
    text_string += "LSC efficiency = " + str(efficiency) + "\n"
    plt.text(0.55, 0.45, text_string, family='monospace', fontsize=9.)
    
    plt.xlabel("horizontal position x [inches]")
    plt.ylabel("vertical position y [inches]")
    
    plt.savefig("hw06plot.png", dpi=300, edgecolor='none')
