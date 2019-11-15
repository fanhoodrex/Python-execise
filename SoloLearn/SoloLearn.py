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
a,b,c = 2,7,2
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

#14 combination
count = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i+j*10+k*100)
                count += 1
print("一共有%d个三位数" % count)

#15 水仙花数
for number in range(100, 1000):
    i = number % 10
    j = number // 10 % 10
    k = number // 100
    if number == i**3+j**3+k**3:
        print(number)

#16 猜字游戏
true_number = int(input("请主持人输入数字："))
low_number = int(input("请主持人输入范围下限："))
high_number = int(input("请主持人输入范围上限："))
i = 1
while i <= 5:
    guess_number = int(input("数字的范围是%d-%d，现在第%d次猜测：" % (low_number, high_number, i)))
    if true_number == guess_number:
        print("恭喜你猜对啦！")
        break
    elif guess_number < true_number and guess_number > low_number:
        low_number = guess_number
    elif guess_number > true_number and guess_number < high_number:
        high_number = guess_number
    i = i + 1
    if i > 5:
        print("很遗憾，你五次都没有猜对。正确数字是%d。" % true_number)

#17 九九乘法表
for i in range(1, 10):
    for j in range(i, 10):
        print("%dx%d=%d" % (i, j, i*j), end="\t")
    print('\n')

#18 ???
x = "abcda"
for i in x:
    if x.index(i) == 0:print(i)

#19 变量内存地址的指针不同
I = [1,9,65,88,4,0]
a = I.sort()
b = sorted(I)
if a == b:
    print(1+1)
else:
    print(0)

#20 ???
print('abef'.partition('cd'))

#21 no output? 
a = 4
b = 2
c = 0
if (a<b) < c:
    print(0)
a,c = c,a
if (a>b)>c:
    print(1)

#22 id of a variable 内存地址一样
x,y =0,True
x = x + 1
y = int(True) # convert bool to value
print(id(x)==id(y))

#23 list + list
a = [1,2,3]
def add(n):
    a += [n]
add(4)
print(a)

#24
a,b,*c = [1,2,3,7]
print(*c) # 3,7
print(c) # list type

#25 ???
print([12,44],[123,'sri',(1,2,3)],'Hello'][2][2][2])

#26 for
b = 3
a = 1
for i in range(b):
    a = a + a*i
print(a)

i= 0,1,2

a = 1
a = 2 
a = 6

#27 ??
def numbers(x):
    for i in range(x):
        if i % 4 ==3:
            yield i
print(list(number(11)))

#28
o = "j"
e = "a"
o = o + e +"v"
o = o + e
m = o
print(m)
o = o + 's'
print(o)
print(m) #

# 29 知识点和28题一样
a = b = 1
b = 2
print(a,b)

#30 anything is value, except None 
def is_it_true(anything):
    if anything:
        print("True")
    else:
        print("False")
is_it_true(None)
is_it_true(1)
is_it_true('str')

#31 ???
def run(a):
    return 2 * a
print(run(run(a)))

#32 math 和 阶乘
import math
print(math.factorial(4.0))

#33 try except handler
import math
try:
    print(math.sqrt(81,'s'),end="")
except:
    print(0,end="")
finally:
    print(x,end="")

#34
a = [8,0,4,6,1]
if (a is a[:]):
    print(True)
else:
    print(False)
print(a[:])

#35
num  = 5
sum = 0
while True:
    if num >= 1:
        sum += num
        num -= 1
    else:
        break
print(sum)

num = 5,4,3,2,1
sum = 5,9,12,14,15

#36
list = [1,2,3,4,6] 
if len(list) % 2 != 0: # len(list) = 5 
    print(list[max(list)%4])
else:
    print(list[min(list)])

max(list) = 6 
max(list)%4 = 2
list[max(list)%4] =3

#37 reverse 
a = [1,2,3,4,5]
print(a[-1:None:-2])
print(a[-1::-2])

#38 ??? 
print(r"\nSololearn")

#39
>>> nums = [1,2,3,3]
>>> max(set(nums), key=nums.count)
3

或者
from collections import Counter
>>> Counter(nums).most_common()[0][0]

#40
>>> d = dict()
>>> d['nums']
KeyError: 'nums'
>>>

>>> from collections import defaultdict
>>> d = defaultdict(list)
>>> d["nums"]
[]

#41
>>> lang = 'python'
>>> f'{lang} is most popular language in the world'
'python is most popular language in the world'

#42
def fun(x):
    if x == 'a':
        return 1
    elif x == 'b':
        return 2
    else:
        return None

def fun(x):
    return {"a": 1, "b": 2}.get(x)

#43
