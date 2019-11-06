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
a = list(a)
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

#20、python2和python3区别？列举5个
"""
1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')
Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hi'
2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存
3、python2中使用ascii编码，python中使用utf-8编码
4、python2中unicode表示字符串序列，str表示字节序列
python3中str表示字符串序列，byte表示字节序列
5、python2中为正常显示中文，引入coding声明，python3中不需要
6、python2中是raw_input()函数，python3中是input()函数
"""

#21、列出python中可变数据类型和不可变数据类型，并简述原理
a,b = 3,3
print(id(a))
print(id(b))

#22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort(reverse=False)
res = "".join(s)
print(res)

#23、用lambda函数实现两个数相乘
sum = lambda a,b:a*b
print(sum(5,4))

#24、字典根据键从小到大排序
dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
lis = sorted(dic.items(),key=lambda i:i[0],reverse= False)
print(lis)
print(dict(lis))

#25、利用collections库的Counter方法统计字符串每个单词出现的次数
#"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter
a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(a)
print(res)

#26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，
#用正则过滤掉英文和数字，最终输出"张三  深圳"
import re
a = "not 404 found 张三 99 深圳"
list = a.split(" ")
print(list)
res = re.findall('\d+[a-zA-Z]+',a)
for i in res:
    if i in list:
        list.remove(i)
new_str = " ".join(list)
print(res,"\n",new_str)

#27、filter方法求出列表所有奇数并构造新列表，
#a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [x for x in range(1,11)]
def fn(a):
    if a%2 == 1:
        return a
newlist = filter(fn,a)
newlist = [i for i in newlist]
print(newlist)

#28、列表推导式求列表所有奇数并构造新列表，
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [x for x in range(1,11)]
res = [i for i in a if i%2==1]
print(res)

#29、正则re.complie作用
#re.compile是将正则表达式编译成一个对象，加快速度，并重复使用

#30、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
a=type((1))
b=type(("1"))
c=type((1,))
print(a,b,c)

#31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
list1 = [i for i in range(1,10,2)]
list2 = [2,2,6,8]
list1.extend(list2)
print(list1)
list1.sort(reverse= False)
print(list1)

#32、用python删除文件和用linux命令删除文件方法
"""
python： os.remove(文件名)
linux: rm  文件名
"""

#33、log日志中，我们需要用时间戳记录error,warning
#等的发生时间，请用datetime模块打印当前时间戳
#“2018-04-01 11:38:54”
import datetime
a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+'  星期:'+str(datetime.datetime.now().isoweekday())
print(a)

#34、数据库优化查询方法
#外键、索引、联合查询、选择特定字段等等

#35、请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
# pychart,matplotlib,seaborn

#36、写一段自定义异常代码
def fn():
    try:
        for i in range(5):
            if i > 2:
                raise Exception("numebr greater than 2")
    except Exception as ret:
        print(ret)
fn()

#37、正则表达式匹配中，（.*）和（.*?）匹配区别？
"""
（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
"""

#38、简述Django的orm
"""
ORM，全拼Object-Relation Mapping，意为对象-关系映射
实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，
而不需要修改代码只需要面向对象编程,
orm操作本质上会根据对接的数据库引擎，翻译成对应的sql语句,
所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，
如果数据库迁移，只需要更换Django的数据库引擎即可
"""

#39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a = [[1,2],[3,4],[5,6]]
x = [j for i in a for j in i]
print(x)

import numpy as np
b = np.array(a).flatten().tolist()
print(b)
#40、x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
x="abc"
y="def"
z=["d","e","f"]
m=x.join(y)
n=x.join(z)
print(m,n)







