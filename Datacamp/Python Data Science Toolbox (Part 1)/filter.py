# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:10:28 2019

@author: Zac_Fang
"""

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member:len(member)>6, fellowship)
# filter out elements from a list that don't satisfy certain criteria.
# keep element that satisfy the condition

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)