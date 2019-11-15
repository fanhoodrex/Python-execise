# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:43:48 2019

@author: Zac_Fang
"""

# Create generator object: result
result = (num for num in range(31))
# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
# Print the rest of the values
for value in result:
    print(value)


# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
# Create a generator object: lengths
lengths = (len(person) for person in lannister)
# Iterate over and print the values in lengths
for value in lengths:
    print(value)
