# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:13:15 2019

@author: Zac_Fang
"""

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

myfunc(*tuple_vec)

myfunc(**dict_vec)