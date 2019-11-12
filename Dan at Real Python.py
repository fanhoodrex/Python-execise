# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:54:10 2019

@author: jfang
"""

vals = [x*x 
        for x in range(10)
        if not x%2]
print(vals)

"""
# This is equivalent to:
vals = []
for value in collection:
    if condition:
        vals.append(expression)
"""

a = {True: 'yes', 1: 'no', 1.0: 'maybe'}
print(a)

def my_add(a: int, b: int) -> int:
    return a + b
my_add(1,2)