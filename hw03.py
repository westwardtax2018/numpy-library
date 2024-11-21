import numpy as np
from math import exp
from hw04_aux import read_headers, read_pressure, read_data, phase_change_index
from fitdata import calc_fit, eval_fit
import matplotlib.pyplot as plt

# ERROR CODE
#  0 => no user errors encountered
#  1 => geopotential elevation is below sea level; P = None
#  2 => geopotential elevation is above lower atmosphere; P = None
ERROR_CODE = 0

# Physical constants
# R = N_A * k from 2022 CODATA Fundamental Physical Constants
R = 8.31446261815324    # molar gas constant [J/mol.K]

# Mean sea level atmospheric data
g0    =      9.80665    # standard gravitational acceleration at sea level [m/s2]
M0    =     28.9586     # standard molecular weight of dry air at sea level [kg/kmol]
P0    = 101325.0        # standard atmospheric pressure at sea level [N/m2]
r_earth = 6356.7523     # earth polar radius (semi-minor axis to mean sea level) [km]

# Table data from Table 4 (page 3) of "US Standard Atmosphere, 1976"
z_table  = np.array([  0.0 ,  11.0 ,  20.0 ,  32.0 ,  47.0 ,  51.0,   71.0 ,  84.852])
T_table  = np.array([288.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65, 186.946])
L_table  = np.array([ -6.5 ,  0.0  ,   1.0 ,   2.8 ,   0.0 ,  -2.8,   -2.0 ,   0.0  ])

# Pressure boundaries computed based on above US Standard Atmosphere 1976 data
P_table  = np.array([1.01325000e+05, 2.26320640e+04, 5.47488867e+03,
                     8.68018685e+02, 1.10906306e+02, 6.69388731e+01,
                     3.95642043e+00, 3.73383590e-01]                )

# -----------------------------------------------------------------------------

# Write function `geometric_to_geopotential_elevation` here

def geometric_to_geopotential_elevation(z):
    """
    converts atm press. for geopot elevation
    z - elev
    p - atmpres
    """
    z_pot = 0.0
    if (z >0.01):
        z_pot = 1/((1/r_earth) + (1/z))
    else:
        z_pot = 0.0
        
    return z_pot


# -----------------------------------------------------------------------------

# Write function `atmospheric_pressure` here
def atmospheric_pressure(z):
    """
    Calculates atm press. for geopot elevation
    z - elev
    p - atmpres
    """
    global ERROR_CODE
    Pressure = 0.0
    
    z_pot = geometric_to_geopotential_elevation(z)
    if z_pot < z_table[0]:
        ERROR_CODE = 1
        return None
    elif z_pot >= z_table[-1]:
        ERROR_CODE = 2
        return None
    
    i = len(z_table) - 1
    while z_pot < z_table[i]:
        if z_pot >= z_table[i-1]:
            lay = i-1
            break
        else:
            i -= 1
    
    z_ti = z_table[lay]
    p_ti = P_table[lay]
    t_ti = T_table[lay]
    l_ti = L_table[lay]
    
    
    if l_ti == 0.0:
        Pressure = p_ti * exp((-g0 * M0 * (z_pot - z_ti)) / (R * t_ti))
    else:
        Pressure = p_ti * ((t_ti / (t_ti + l_ti * (z_pot - z_ti))) ** ((g0 * M0) / (R * l_ti)))
        
    return Pressure
            
# =============================================================================
# Design Calculations
# =============================================================================

# Rocket nozzel design data
gamma = 1.4       # specific heat ratio (cp/cv)
Pc    = 1.825e7   # combustion pressure [Pa]
Ath   = 0.1       # throat area [m2]

# Write function `eq2` here.  This one's free.
# Feel free to change the variable names, but keep
# the function name and the quantity returned the same.
def eq2(M):
    """Computes exit pressure from Mach number.
    
    Based on module variables Pc and gamma.
    
    INPUT:  M  - Mach number [-]
    OUTPUT: Pe - pressure at exit of nozzle [Pa]
    """
    Pe = Pc * (1 + ((gamma-1)/2) * M**2) ** (-gamma / (gamma - 1))
    return Pe

# Write function `eq3` here
# Use lots of intermediate variables to break it up
# into factors if that's easier.  Develop your own
# style for how to check and re-check what you enter.
def eq3(M):
    """
    

    Parameters
    ----------
    M : TYPE
        DESCRIPTION.

    Returns
    -------
    Ae : TYPE
        DESCRIPTION.

    """
    Ae = Ath * (1/M) * ((gamma + 1) / 2) ** ((-(gamma + 1))/(2*(gamma-1))) * (1+((gamma - 1) / 2)*(M*2)) ** ((gamma+1) / (2*(gamma - 1)))
    return Ae



# Write function `scoping_design` as shown below and described
# in the assignment statement.  Make sure your file `find_root`
# is in the same directory.

def scoping_design():
    """
    Input: none.
    Output: four arrays of output are returned from this function in the following order on the
    return statement. 


    Returns
    -------
    None.

    """
    
    from find_root import bisection

    # Initialize arrays of z, Ae, M, and P with the geometric
    # elevation ranging from 0.0 to 80.0 km with 41 points
    # in each array (=> 2 km intervals).  The elevation array
    # should be filled here; the others will be computed
    # element by element in the loop.
    
    # Loop over array of geometric elevations to compute results at

        # calculate atmospheric pressure as a function of elevation
        
        # set up residual function as a lambda function
        
        # apply bisection method to solve for mach number
        # M will never be less than or equal to 1.0 or
        #    the nozzle exit will not be supersonic
        # M shouldn't be greater than 30, the extreme ratio
        #    claimed by the fastest wind tunnel in the world

    
        # compute exit area based on mach number

    # return arrays of z, Ae, M, and P, in that 
    z_list = np.linspace(0.0, 80.0, 41)
    Ae = np.zeros(41)
    p_list = np.zeros(41)
    M = np.zeros(41)
    
    def eq_1(M, P):
        change = eq2(M) - P
        return change
    for i in range(0, z_list.size):
        P = atmospheric_pressure(z_list[i])
        p_list[i] = P
        bisection_func = lambda M: eq_1(M, P)
        M[i] = bisection(bisection_func, 1.01, 30)
        Ae[i] = eq3(M[i])
        
    return z_list, Ae, M, p_list

# -----------------------------------------------------------------------------

# Tabulating and plotting the results to consider your conclusions.
# Uncomment the statements below to run scoping design and plot
# the results.
#
# Uncomment the next block of statements below to get
# tabular output.  Be sure to comment before submission.
#
# Select results:  
#          z       Ae       M        Pe
#       ------ ---------- ------- --------
#         0.0     1.2020   4.129  101325.0
#

# elevations, exit_areas, mach_numbers, P = scoping_design()
#
# print("    z       Ae        M       Pe   ")
# print(" ------ ---------- ------- --------")
# for i in range(0, elevations.size, 10):
#     print('{: 6.1f}'.format(elevations[i])  ,
#           '{:10.4f}'.format(exit_areas[i])  ,
#           '{: 7.3f}'.format(mach_numbers[i]),
#           '{: 9.1f}'.format(P[i])            )
#
# import matplotlib.pyplot as plt
# plt.figure(1, figsize=(7, 4))
# plt.yscale('log')
# plt.plot(elevations, exit_areas, color="red", linestyle="-", lw=2)
# plt.xlabel("elevation, z [km]")
# plt.ylabel("exit area, $A_e$ [$m^2$]")
# plt.title("Rocket converging-diverging nozzle exit area morphing with elevation")
# plt.grid(True)
# text_string =  "Look at the plot and think:\n"
# text_string += "is it a good idea to use a\n"
# text_string += "single stage rocket of\n"
# text_string += "this design?"
# plt.text(10, 90, text_string)
# plt.show()


MAKE_PLOT = False
FILENAME = "sos-water.csv"
DATA_SET = 3  # For submission, use 3
  # Example values

# 2. Read data
headers = read_headers(FILENAME)
pressure = read_pressure(DATA_SET, headers)
T, sos = read_data(FILENAME, DATA_SET)

# 3. Identify phase change index
phase_index = phase_change_index(T)

# 4. Calculate polynomial fits
liquid_coeffs = calc_fit(T[:phase_index], sos[:phase_index], degree=DEGREE_FITS[DATA_SET - 1][0])
vapor_coeffs = calc_fit(T[phase_index:], sos[phase_index:], degree=DEGREE_FITS[DATA_SET - 1][1])

# 5. Plotting
if MAKE_PLOT == True:
    plt.scatter(T, sos, label='Data', color='blue')
    # Generate fit values for plotting
    T_fit = np.linspace(min(T), max(T), 100)
    sos_fit_liquid = eval_fit(liquid_coeffs, T_fit[T_fit <= T[phase_index]])
    sos_fit_vapor = eval_fit(vapor_coeffs, T_fit[T_fit > T[phase_index]])
    plt.plot(T_fit[T_fit <= T[phase_index]], sos_fit_liquid, label='Liquid Fit', color='red')
    plt.plot(T_fit[T_fit > T[phase_index]], sos_fit_vapor, label='Vapor Fit', color='green')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Speed of Sound (m/s)')
    plt.title(f'Speed of Sound in Water at {pressure} MPa')
    plt.legend()
    plt.show()














