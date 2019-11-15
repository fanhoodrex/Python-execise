# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:45:21 2019

@author: Zac_Fang
"""
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
# Print each list item in flash using a for loop
for person in flash:
    print(person)
# Create an iterator for flash: superspeed
superspeed = iter(flash)
# Print each item from the iterator
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))

avengers = ['hawkeye','iron man','thor','quicksilver']
x = iter(avengers)
for i in range(3):
    print(next(x))
    
# Create a range object: values
values = range(10,21)
# Print the range object
print(values)
# Create a list of integers: values_list
values_list = list(values)
# Print values_list
print(values_list)
# Get the sum of values: values_sum
values_sum = sum(values)
# Print values_sum
print(values_sum)

