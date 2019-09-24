#1 tuple catenation
a=5,
b=6,7
c=a+b
print(c)

#2 list of set
a = [{x*2,x+2}for x in range(5)]
print(a)
print(type(a[1]))

#3 order
a,b,c = 2,7
print(a+b*a//c)
a*b//c
a*c//b

#4 use of lambda
a=(lambda x:x**3)((lambda x:x+2)(1))
print(a)

#5 use of built-in module itertools
import itertools
original_list = [[2,4,3],[1,5,6]]
new_list = list(itertools.chain(*original_list))
print(new_list)

#6 reverse of number
n = 123
result = 0
while(n>0):
    remainder = int(n % 10)
    result = result * 10 + remainder
    n = int(n/10)
print(result)

#7 round off ceil or down
def ok_then_call(s,num):
    return s + str(float(int(num/2)))
s = 'test'
data = ok_then_call(s,11)
print(data)

#8 Bitwise Operators | means OR
a = set([1,2,3,4])
b = set([1,2,5,6])
x = a | b
y = a & b
print(len(x))

#9 use of built-in module fraction
from fractions import Fraction
frac = Fraction(1,3)
frac = frac + 2
frac = frac + Fraction(2,3)
print(frac)

# 10 Precedence order of Python Operators
3*1**3

#11 use of function
def fun(a):
    x = a ** 2
    y = 0
    while x>1:
        x -= 1
        y += 2
    return y
print(fun(1)+fun(2))

#12 list method and object address: b point to a address
a = [1,2,3]
b = a
a.append(10)
print(len(b))

#13 dictionary key lookup
tup = (1,2,3,4,5,6)
tab = [1,2,3,4,5,6]
dic = {1:2,3:4,5:6}
print(tup[1] + tab[2] + dic[3])

#14
