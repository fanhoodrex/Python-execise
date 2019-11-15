# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 01:48:23 2019

@author: Zac_Fang
"""
import operator
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(xs.items(), key=lambda x: x[1])

sorted(xs.items(), key=operator.itemgetter(1))