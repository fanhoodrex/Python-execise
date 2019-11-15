# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:03:25 2019

@author: Zac_Fang
"""

my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}

import json
print(json.dumps(my_mapping,indent=4,sort_keys=True))
