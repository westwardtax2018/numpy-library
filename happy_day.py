"""A Plot for February 14th"""

import numpy as np
import matplotlib.pyplot as plt

def crazy_on_you(x):
    """The band, with x in radians.

    Input:   x coordinate in range -1.56 to +1.56
    Output:  y coordinate of a greeting card plot
    """
    import numpy as np
    y = np.sqrt(np.cos(x))*np.cos(90.0*x)+np.sqrt(np.abs(x))
    return y

# abs(x) < 1.56 avoids NaN warnings outside that range
# <500 points has increasingly problematic discretization error
x = np.linspace(-1.56, 1.56, 500)
y = crazy_on_you(x)

plt.figure(1, figsize=(6, 4))
plt.plot(x, y, '-r')          # red, of course

plt.title( "For you..." , fontsize=14)
plt.xlabel("now"        , fontsize=12)
plt.ylabel("and forever", fontsize=12)

# save to file if desired
# =============================================================================
# True  - displays and saves the plot to file;
# False - only displays the plot
save_plot_to_file = True
filename = 'happy_day.png'
# =============================================================================
if (save_plot_to_file):
    plt.savefig(filename, dpi=300, edgecolor='none')
plt.show()