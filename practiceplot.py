# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:06:44 2024

@author: banerm
"""

import matplotlib.pyplot as plt

save_plot_to_file = True
filename = 'practice_plot.png'
# ==================================================
if (save_plot_to_file):
 plt.savefig(filename, dpi=300, edgecolor='none')
plt.show()