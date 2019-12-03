# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:17:17 2019

@author: jfang
"""

# Import pandas as pd
import pandas as pd
# Assign the filename: file
file = 'titanic.csv'
# Read the file into a DataFrame: df
df = pd.read_csv(file)
# View the head of the DataFrame
print(df.head())
