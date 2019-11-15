# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:18:28 2019

@author: Zac_Fang
"""

# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1,item2:item1 + item2, stark,'initial_value:')

# Print the result
print(result)