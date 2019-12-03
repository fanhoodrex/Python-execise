# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:16:42 2019

@author: jfang
"""

# Assign the filename: file
file = 'titanic.csv'
# Import file using np.recfromcsv: d
d = np.recfromcsv(file)
# Print out first three entries of d
print(d[:3])
