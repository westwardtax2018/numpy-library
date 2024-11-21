"""Sample case for Lagrange Interpolation"""

import numpy as np
import matplotlib.pyplot as plt
from lagrange import interpolate

# Steam Table Data
TC = np.array([ 0.01,  5., 10., 15., 20.,
               25.  , 30., 35., 40., 45.,
               50.  , 55., 60., 65., 70.,
               75.  , 80., 85., 90., 95. ])

P_sat = np.array([ 0.6113,  0.8721,  1.2276,  1.7051,  2.339,
                   3.169 ,  4.246 ,  5.628 ,  7.384 ,  9.593,
                  12.349 , 15.758 , 19.940 , 25.03  , 31.19 ,
                  38.58  , 47.39  , 57.83  , 70.14  , 84.55  ])

xdata =    TC
ydata = P_sat

# interpolation curve
xeval = np.linspace(TC[0]-3., TC[-1]+3., 100)
yeval = interpolate(xdata, ydata, xeval)

# plot interpolation data and interpolant
fig = plt.figure(1, figsize=(6, 4))
plt.plot(xdata, ydata, 'bo', label='measured thermodynamic data')
fit_label = "Lagrange interpolant"
plt.plot(xeval, yeval, 'r-', linewidth = 2.0, label=fit_label)

# text box with sample single interpolation
T = 22.5
xeval = np.array([T])
P = interpolate(xdata, ydata, xeval)[0]
string  = "T [C] = "
string += "{:.2f}".format(T)
string += " and Psat [kPa] = "
string += "{:.4f}".format(P)
plt.text(5., 45., string, fontsize=10,
            bbox={'facecolor': 'black', 'alpha': 0.04, 'pad': 2})
plt.plot([T, T], [-5.0, 40.], 'c--')

# set plot bounds and draw grid
plt.xlim([-5.0, 100.0])
plt.ylim([-5.0, 100.0])
plt.gca().grid()

# plot axis labels, legend, title, and text box
plt.rcParams['font.family'] = "Consolas"
plt.xlabel('temperature, T [C]', fontsize=12)
plt.ylabel('saturation pressure, $P_{sat}$ [kPa]', fontsize=12)
plt.legend(fontsize=10, loc=2)

string  = "water saturation pressure"
plt.title(string, fontsize=14)

plt.show()