from random import random
from math import sqrt
import time
darts = 100000
hits=0
time.clock()
for i in range(1,darts+1):
    x,y=random(),random()
    dist=sqrt(x**2+y**2)
    if dist<=1.0:
        hits+=1
pi=4*(hits/darts)
print("Pi'value is {}".format(pi) )
print("it takes :{:.5f}s".format(time.clock()))
