# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:13:07 2019

@author: jfang
"""
# Open a file: file
file = open('moby_dick.txt',mode='r')
# Print it
print(file.read())
# Check whether file is closed
print(file.closed)
# Close file
file.close()
# Check whether file is closed
print(file.closed)

