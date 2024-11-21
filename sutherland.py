# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:37:59 2024

@author: banerm
"""
S = 110.4
C1 = 1.458e-6
v = 0.0 

"""
sutherland.py

This module provides a function to calculate the viscosity of a gas 
using Sutherland's formula. It can also be executed from the command 
line to compute viscosity for a given temperature.
"""


def calc_viscosity(temperature):
  
  """ calculating the viscosity using temperature and setting viscosity as float """
  v = (C1 * temperature**(3/2)) / (temperature + S)
  return v

if __name__ == "__main__":   # if run from command prompt
# get temperature, `T`, from command line and compute
    import sys
    T = float(sys.argv[1])   # convert string to float
    mu = calc_viscosity(T)   # compute viscosity
    print(mu)