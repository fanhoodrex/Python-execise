import numpy as np
import time 
import sys 
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z=np.array([x,y])
print(z.shape)
print ("hello")
#------------------------------------------------

size=100

l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

#python list
start = time.time()
result=[(x+y)for x,y in zip()11,12]
print("python list took:",(time.time()-start)*1000)
#numpy array
start=time.time()
result=a1+a2
print("numpy took",(time.time()-start)*1000)
