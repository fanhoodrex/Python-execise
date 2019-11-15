# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:54:18 2019

@author: Zac_Fang
"""
# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']
#Create and print the enumerate object
mutant_enum = enumerate(mutants)
print(mutant_emu)
# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))
# Print the list of tuples
print(mutant_list)
# Unpack and print the tuple pairs
for index1,value1 in enumerate(mutants): #unpack the tuple pair
    print(index1, value1)
# Change the start index
for index2,value2 in enumerate(mutants,start=1):
    print(index2, value2)


# Create a list of tuples: mutant_data
mutants = list(range(1,6))
aliases = list(range(6,11))
powers = list(range(11,16))
mutant_data = list(zip(mutants,aliases,powers))
# Print the list of tuples
print(mutant_data)
# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants,aliases,powers)
# Print the zip object
print(mutant_zip)
# Unpack the zip object and print the tuple values
for value1,value2,value3 in mutant_zip:
    print(value1, value2, value3)


# Create a zip object from mutants and powers: z1
mutants = range(1,6)
powers = range(11,16)
z1 = zip(mutants,powers)
# Print the tuples in z1 by unpacking with *
print(*z1)
# Re-create a zip object from mutants and powers: z1 
"""Because the previous print() call would have exhausted the elements in z1, 
recreate the zip object you defined earlier and assign the result again to z1"""
z1 = zip(mutants,powers)
# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1,result2 = zip(*z1)
# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)


avengers = ['hawkeye','iron man','thor','quicksilver']
e = enumerate(avengers)
print(type(e))
e_list = list(e)
print(e_list)
for index,value in enumerate(avengers,start=1):
    print(index,value)
for index,value in enumerate(avengers,start=10):
    print(index,value)