# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:24:29 2019

@author: jfang
"""

# Make a string with the value 'PA': state
state = 'PA'
# Construct a dictionary: data
data = {'state':state, 'city':cities}
# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)
# Print the DataFrame
print(df)