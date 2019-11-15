# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:10:32 2019

@author: Zac_Fang
"""

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted_xs=sorted(xs.items(), key=lambda x: x[1])
print(sorted_xs)

import operator
sorted_item=sorted(xs.items(), key=operator.itemgetter(1))
print(sorted_item)