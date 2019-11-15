# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:04:45 2019

@author: Zac_Fang
"""
# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1,echo : word1*echo)

# Call echo_word: result
result = echo_word('hey',5)

# Print result
print(result)

a = lambda x:x+1
g = (lambda x:x*2)
#with or without parenthese is no different

a(3)
b = a(5)
print(b)