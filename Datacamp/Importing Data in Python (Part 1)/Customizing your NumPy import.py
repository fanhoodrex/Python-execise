# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:15:24 2019

@author: jfang
"""
# Import numpy
import numpy as np
# Assign the filename: file
file = 'digits_header.txt'
# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])
# Print data
print(data)
