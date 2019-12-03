# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:18:22 2019

@author: jfang
"""

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt,pandas as pd
# Assign filename: file
file = 'titanic_corrupt.txt'
# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')
# Print the head of the DataFrame
print(data.head())
# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
