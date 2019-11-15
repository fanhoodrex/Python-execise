# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:03:32 2019

@author: Zac_Fang
"""

avengers = ['hawkeye','iron man','thor','quicksilver']
name = ['barton','stark','odinson','maximoff']

# iterator of tuple
z = zip(avengers,name)
print(*z) # spla, which is same as the print(list(z)) 
print(z) 
print(list(z))
print(type(z))
for z1,z2 in zip(avengers,name):
    print(z1,z2)