"""A solution to hw04: a module to fit and plot water speed of sound data."""

# =============================================================================
# IMPORT LIBRARIES AS NEEDED
# DO _NOT_ IMPORT matplotlib HERE (SEE THE INSTRUCTIONS)
# =============================================================================

import numpy as np
from hw04_aux import read_headers, read_pressure, read_data, phase_change_index, end_of_data_index
from fitdata import calc_fit, eval_fit


# =============================================================================
# SET DEBUG, FILENAME, and DATA SET SELECTION
# ALSO PROVIDE DEGREES OF POLYNOMIALS TO USE FOR FITS
# =============================================================================
debug_functions   = False
debug             = False
save_plot_to_file = False

MAKE_PLOT   = False
FILENAME    = "sos-water.csv"
DATA_SET    = 3

# These integer polynomial degrees should be high enough
# that the fit closely follows the trend of the data to
# the eye, but low enough that the fit is parsimonious
# (i.e., of the lowest degree that shows no significant
# visible change to the fit)
#
DEGREE_FITS = np.array([[ 2,  1],
                        [ 3,  2],
                        [ 3,  2],
                        [ 4,  3] ])

# =============================================================================
# READ AND PROCESS DATA
# =============================================================================

# obtain headers from all of the data sets
headers = read_headers(FILENAME)




# extract pressure from the header for the selected data set
pressure = read_pressure(DATA_SET, headers)


# get temperature and speed of sound data
T, sos = read_data(FILENAME, DATA_SET)
# *** Placeholder data!
placeholder_T_array   = np.array([ 273.16,  283.16,  293.16,  303.16,  313.16])
placeholder_sos_array = np.array([1402.4 , 1447.3 , 1482.4 , 1509.2 , 1528.9 ])

 
# find piecewise data ranges
phase_index = phase_change_index(T)
end_data = end_of_data_index(T)

# =============================================================================
# MAKE FITS
# =============================================================================



# compute the polynomial coefficients for the liquid water slice of the data
liquid_coeffs = calc_fit(T[:phase_index-1], sos[:phase_index-1], degree=DEGREE_FITS[DATA_SET - 1, 0])
liquid_sos = eval_fit(liquid_coeffs, T[:phase_index - 1])


# compute the polynomial coefficients for the vapor water slice of the data

vapor_coeffs = calc_fit(T[phase_index:end_data], sos[phase_index:end_data], degree=DEGREE_FITS[DATA_SET - 1, 1])
vapor_sos = eval_fit(vapor_coeffs, T[phase_index:end_data] )

# =============================================================================
# MAKE PLOT
# =============================================================================

if (MAKE_PLOT):
    import matplotlib.pyplot as plt

    # start plot
    plt.figure(1, figsize=(6, 4))
    
    # plot the data as black dots
    data_label = "measured data"
    plt.plot(T, sos, 'k.', label=data_label)
    
    # plot the liquid fit as a blue line only on the data
    # *** Note placeholder data!
    #placeholder_x_array = [ 300.,  400.,  500.]
   # placeholder_y_array = [1300., 1400., 1500.]
    liq_fit_label  = "liquid region, fit degree = " + str(DEGREE_FITS[DATA_SET -1, 0]) 
    plt.plot(T[:phase_index - 1], liquid_sos, "b-", label=liq_fit_label)
    
    # plot the vapor fit as a red line only on the data
    # *** Note placeholder data!
    #placeholder_x_array = [700., 800., 900.]
    #placeholder_y_array = [700., 800., 900.]
    vap_fit_label  = "liquid region, fit degree = " + str(DEGREE_FITS[DATA_SET - 1, 1])
    plt.plot(T[phase_index: end_data], vapor_sos, "r-", label=vap_fit_label)
    
    # set plot bounds and draw grid
    plt.xlim([250.0, 1050.0])
    plt.ylim([  0.0, 2000.0])
    plt.gca().grid()
    
    # plot axis labels, legend, title, and text box
    plt.rcParams['font.family'] = "Consolas"
    plt.xlabel('temperature, T [K]', fontsize=12)
    plt.ylabel('speed of sound, C, [m/s]', fontsize=12)
    plt.legend(fontsize=10, loc=1)
    
    title_string  = "Speed of Sound in Water at " + str(pressure) + " [MPa]"
    plt.title(title_string, fontsize=14)
    
    np.set_printoptions(precision=1)
    phase_string  = "Phase Transition is at " + str(T[phase_index]) + " [K]"
    phase_string += "\n liquid fit: " + str(liquid_coeffs)
    phase_string += "\n vapor fit: " + str(vapor_coeffs)
    plt.text(270., 70., phase_string, fontsize=10,
                bbox={'facecolor': 'black', 'alpha': 0.04, 'pad': 2})
    
    if (save_plot_to_file):
        plt.savefig('plot.png', dpi=300, edgecolor='none')
    plt.show()

