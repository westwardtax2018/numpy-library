# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:04:27 2024

@author: banerm
"""
import numpy as np
"""
hw04_aux.py

This module contains functions for reading and processing speed of sound data from a CSV file 
specific to water's thermodynamic properties. It provides utilities to extract headers, pressures, 
and data from the specified dataset.
"""

def read_headers(filename, print_headers=False):
    """
    Read the headers from the first row of a CSV file.

    This function extracts the column headers from the specified CSV file. It reads only the first 
    row and returns the headers as a 1D array of strings.

    Parameters:
    filename : str
        The name of the file to read headers from.
    print_headers : bool, optional
        If True, prints the headers to the screen for debugging (default is False).

    Returns:
    headers : ndarray
        A 1D array of strings representing the column headers.
    """
    headers = np.loadtxt(filename, max_rows=1, delimiter=",", dtype=str)
    if print_headers:
        print(headers)
    return headers

def read_pressure(data_set, headers, print_pressure=False):
    """
    Extract the pressure corresponding to a specified data set from headers.

    This function identifies the pressure associated with the given data set index by parsing 
    the corresponding header string. It extracts and returns the pressure value as a float.

    Parameters:
    data_set : int
        The index of the data set (1 to 5).
    headers : ndarray
        A 1D array of strings containing column headers.
    print_pressure : bool, optional
        If True, prints the pressure for debugging (default is False).

    Returns:
    P : float
        The pressure associated with the specified data set.
    """
    index = (data_set - 1) * 2  # Each data set has 2 columns for temperature and speed of sound
    pressure_str = headers[index].split('(')[1].split(')')[0]
    P = float(pressure_str)
    if print_pressure:
        print(f'Pressure for dataset {data_set}: {P} MPa')
    return P

def read_data(filename, data_set, print_data=False):
    """
    Read temperature and speed of sound data for a specified data set from a CSV file.

    This function extracts the temperature and speed of sound data corresponding to the provided 
    data set index. It reads the appropriate columns and returns them as two separate 1D arrays.

    Parameters:
    filename : str
        The name of the file to read data from.
    data_set : int
        The index of the data set (1 to 5).
    print_data : bool, optional
        If True, prints the data to the screen for debugging (default is False).

    Returns:
    T : ndarray
        A 1D array of temperature data.
    sos : ndarray
        A 1D array of speed of sound data.
    """
    cols = [(data_set - 1) * 2, (data_set - 1) * 2 + 1]
    data = np.loadtxt(filename, skiprows=1, delimiter=",", usecols=cols)
    T, sos = data[:, 0], data[:, 1]
    if print_data:
        print(f'Temperature Data: {T}')
        print(f'Speed of Sound Data: {sos}')
    return T, sos

def phase_change_index(T, print_index=False):
    """
    Identify the index where the phase change occurs in the temperature data.

    This function scans the temperature array for the first occurrence of two consecutive 
    temperatures that are equal within a precision of 0.01, indicating a phase change from 
    liquid to vapor. It returns the index of the first vapor temperature.

    Parameters:
    T : ndarray
        A 1D array of temperature data.
    print_index : bool, optional
        If True, prints the index for debugging (default is False).

    Returns:
    index : int
        The index of the first vapor temperature, or -1 if no phase change is detected.
    """
    for i in range(len(T) - 1):
        if abs(T[i] - T[i + 1]) < 0.01:
            if print_index:
                print(f'Phase change index found at: {i + 1}')
            return i + 1
    return -1

def end_of_data_index(T, print_index=False):
    """
    Identify the index of the first negative temperature in the data.

    This function scans the temperature array for the first occurrence of a negative value, 
    which indicates that there is no more valid data. If no negative values are found, it returns 
    the length of the array, which represents the index one greater than the last valid data point.

    Parameters:
    T : ndarray
        A 1D array of temperature data.
    print_index : bool, optional
        If True, prints the index for debugging (default is False).

    Returns:
    index : int
        The index of the first negative temperature, or the length of T if no negatives are found.
    """
    for i in range(len(T)):
        if T[i] < 0:
            if print_index:
                print(f'End of data index found at: {i}')
            return i
    if print_index:
        print('No negative values found. Returning length of array.')
    return len(T)

