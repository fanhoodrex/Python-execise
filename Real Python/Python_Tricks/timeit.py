# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:46:08 2019

@author: Zac_Fang
"""

import timeit
a = timeit.timeit('"-".join(str(n) for n in range(100))',number=10000)
b = timeit.timeit('"-".join([str(n) for n in range(100)])',number=10000)
c = timeit.timeit('"-".join(map(str, range(100)))',number=10000)
print(a,b,c)