# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#1、一行代码实现1--100之和
print(sum(range(1,101)))

#2、如何在一个函数内部修改全局变量
a = 5 
def fn():
    global a 
    a = 4
fn()
print(a)

#3、
#列出5个python标准库
# 5 python standard library
# os sys re math datetime

#4、字典如何删除键和合并两个字典
dic1 = {"name":"zs","age":18}
del dic1["name"]
print(dic1)
dic2 = {"name":"1s"}
dic1.update(dic2) # merger two dictionary\
dic_merge = {**dic1,**dic2}
print(dic1)
print(dic_merge)

#5、谈下python的GIL
"""GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，
一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），
使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，
则解释器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。
多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，
所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大"""

#6、python实现列表去重的方法
list = [11,12,13,12,15,16,13]
a = set(list)
print(a)
print([x for x in a])

#7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
def demo(args_f,*args_v):
    print(args_f)
    for x in args_v:
        print(x)
demo('a','b','c','d')

def demo(**args_v):
    for k,v in args_v.items():
        print(k,v)
demo(name='njcx')

#8、python2和python3的range（100）的区别
#python2返回列表，python3返回迭代器，节约内存

#9、一句话解释什么样的语言能够用装饰器?
#函数可以作为参数传递的语言，可以使用装饰器

#10、python内建数据类型有哪些
"""
整型--int
布尔型--bool
字符串--str
列表--list
元组--tuple
字典--dict
"""

#11、简述面向对象中__new__和__init__区别

#12、简述with方法打开处理文件帮我我们做了什么？
f = open("./1.txt","wb")
try:
    f.write("Hello World")
except:
    pass
finally:
    f.close()

#13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，
#并使用列表推导式提取出大于10的数，最终输出[16,25]
lis = [1,2,3,4,5,6]
def fn(x):
    return x**2
map_list = map(fn,lis)
print(map_list)
map_list = [i for i in map_list if i > 10] 
# reassignment using list comprehension
print(map_list)

#14、python中生成随机整数、随机小数、0--1之间小数方法
import random
import numpy as np
result = random.randint(10,20)
res = np.random.randn(5)
ret = random.random()
print("正整数:",result)
print("5个随机小数:",res)
print("0-1随机小数:",ret)

#15、避免转义给字符串加哪个字母表示原始字符串？
# r , 表示需要原始字符串，不转义特殊字符

#16、<div class="nam">中国</div>，
#用正则匹配出标签里面的内容（“中国”），
#其中class的类名是不确定的
import re
str = '<div class="nam">China</div>'
res = re.findall(r'<div class=".*">(.*?)</div>',str)
print(res)

#17、python中断言方法举例
a = 3 
assert(a>1)
print("assertation correct, proceed with next")

b = 4
assert(b>7)
print("assertation wrong,program error")

# 18、数据表student有id,name,score,city字段，
#其中name中的名字可有重复，需要消除重复行,请写sql语句
# select distinct(name) from student

#19、10个Linux常用命令
"""ls  pwd  cd  touch  rm  mkdir  tree  
cp  mv  cat  more  grep  echo"""













