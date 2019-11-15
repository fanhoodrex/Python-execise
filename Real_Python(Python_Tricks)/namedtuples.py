# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:32:11 2019

@author: Zac_Fang
"""
# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
from collections import namedtuple
Car = namedtuple('Car','color mileage')

# Our new "Car" class works as expected:
my_car = Car('red',3812.4)
print(my_car.color)
print(my_car.mileage)

# We get a nice string repr for free:
Car(color='red',mileage = 3812.4)

# Like tuples, namedtuples are immutable:
my_car.color = 'blue'