#1
import itertools
original_list = [[2,4,3],[1,5,6]]
new_list = list(itertools.chain(*original_list))
print(new_list) 

#2
a,b,c = 2,7,8
print(a+b*a//c) #
a*b//c
a*c//b

#3
a=(lambda x:x**3)((lambda x:x+2)(1))
print(a)

#4
