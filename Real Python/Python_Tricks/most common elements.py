# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# collections.Counter lets you find the most common
# elements in an iterable:

import collections
c = collections.Counter('helloworld')
print(c)
print(c.most_common(3))