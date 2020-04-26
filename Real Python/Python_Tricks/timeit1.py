# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 03:03:41 2019

@author: Zac_Fang
"""
import timeit
timeit,timeit('"-".join(str(n) for n in range(100))',number=10000)
timeit.timeit('"-".join([str(n) for n in range(100)])',number=10000)
timeit.timeit('"-".join(map(str, range(100)))',number=10000)

