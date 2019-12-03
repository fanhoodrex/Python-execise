# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:17:34 2019

@author: jfang
"""
import pandas as pd
# Assign the filename: file
file = 'digits.csv'
# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file,nrows=5,header=None)
# Build a numpy array from the DataFrame: data_array
data_array = data.values

# Print the datatype of data_array to the shell
print(data_array)
print(type(data_array))