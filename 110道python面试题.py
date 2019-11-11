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

#41、举例说明异常模块中try except else finally的相关意义
"""
try..except..else没有捕获到异常，执行else语句
try..except..finally不管是否捕获到异常，都执行finally语句
"""
try:
    num = 100
    print(num)
except NameError as errorMsg:
    print("generate error:%s"%errorMsg)
else:
    print("no error caught, proceed with this statement")
finally:
    print("finally")

try:
    num = 100
    print(num)
except NameError as errorMsg:
    print("generate error:%s"%errorMsg)
finally:
    print("generate this whatever happen")

#42、python中交换两个数值
a,b=3,4
print(a,b)
a,b = b,a
print(a,b)    

#43、举例说明zip（）函数用法
a = [1,2]
b = [3,4]
c = zip(a,b)
res = [i for i in zip(a,b)]
print(res)

a = (1,2)
b = (3,4)
res = [i for i in zip(a,b)]
print(res)

a = "ab"
b = "xyz"
res = [i for i in zip(a,b)]
print(res)

#44、a="张明 98分"，用re.sub，将98替换为100
import re
a = "张明 98分"
ret = re.sub(r"\d+","100",a)
print(ret)

#45、写5条常用sql语句
"""
show databases;
show tables;
desc 表名;
select * from 表名;
delete from 表名 where id=5;
update students set gender=0,hometown="北京" where id=5
"""

#46、a="hello"和b="你好"编码成bytes类型
a=b"hello"
b="哈哈".encode()
print(a,b)
print(type(a),type(b))

#47、[1,2,3]+[4,5,6]的结果是多少？
#两个列表相加，等价于extend
a = [1,2,3]
b = [4,5,6]
res = a + b
print(res)

#48、提高python运行效率的方法
"""
1、使用生成器，因为可以节约大量内存
2、循环代码优化，避免过多重复代码的执行
3、核心模块用Cython  PyPy等，提高效率
4、多进程、多线程、协程
5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率
"""

#49、简述mysql和redis区别
"""
redis： 内存型非关系数据库，数据保存在内存中，速度快
mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的Io操作，访问速度相对慢
"""

#50、遇到bug如何处理
"""
1、细节上的错误，通过print（）打印，能执行到print（）说明一般上面的代码没有问题，分段检测程序是否有问题，如果是js的话可以alert或console.log
2、如果涉及一些第三方框架，会去查官方文档或者一些技术博客。
3、对于bug的管理与归类总结，一般测试将测试出的bug用teambin等bug管理工具进行记录，然后我们会一条一条进行修改，修改的过程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，我也都会收藏做一些笔记记录。
4、导包问题、城市定位多音字造成的显示错误问题
"""

#51、正则匹配，匹配日期2018-03-20
import re
url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
result = re.findall(r'dateRange=(.*?)%7C(.*?)&',url)
print(result)

#52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
list = [2,3,5,4,9,6]
new_list = []
def get_min(list):
    #get the smallest value
    a = min(list)
    #delete samllest value
    list.remove(a)
    #add the smallest value to the new list
    new_list.append(a)
    #ensure the existence of the last value in the list 
    #recursively calling function to get the smallest value
    #until the exhause 
    if len(list) > 0:
        get_min(list)
    return new_list

new_list = get_min(list)
print(new_list)

#53、写一个单列模式
class Singleton(object):
    __instance = None
    def __new__(cls,age,name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
a = Singleton(18,"dougGe")
b = Singleton(8,"douGe")

print(id(a))
print(id(b))

a.age = 19 #给a指向的对象添加一个属性
print(b.age)#获取b指向的对象的age属性

#54、保留两位小数
a = "%.o3f"%1.3335
print(a,type(a))
b = round(float(a),1)
print(b)
b = round(float(a),2)
print(b)

A = zip(("a","b","c","d","e"),(1,2,3,4,5))
A0 = dict(A)
#print(A0)

#55、求三个方法打印结果
def fn(k,v,dic={}):
    dic[k]=v
    print(dic)
fn("one",1)
fn("two",2)
fn("three",3,{})

#56、列出常见的状态码和意义
"""
200 OK 
请求正常处理完毕

204 No Content 
请求成功处理，没有实体的主体返回

206 Partial Content 
GET范围请求已成功处理

301 Moved Permanently 
永久重定向，资源已永久分配新URI

302 Found 
临时重定向，资源已临时分配新URI

303 See Other 
临时重定向，期望使用GET定向获取

304 Not Modified 
发送的附带条件请求未满足

307 Temporary Redirect 
临时重定向，POST不会变成GET

400 Bad Request 
请求报文语法错误或参数错误

401 Unauthorized 
需要通过HTTP认证，或认证失败

403 Forbidden 
请求资源被拒绝

404 Not Found 
无法找到请求资源（服务器无理由拒绝）

500 Internal Server Error 
服务器故障或Web应用故障

503 Service Unavailable 
服务器超负载或停机维护
"""

#57、分别从前端、后端、数据库阐述web项目的性能优化
"""
前端优化：
1、减少http请求、例如制作精灵图
2、html和CSS放在页面上部，javascript放在页面下面，因为js加载比HTML和Css加载慢，所以要优先加载html和css,以防页面显示不全，性能差，也影响用户体验差

后端优化：
1、缓存存储读写次数高，变化少的数据，比如网站首页的信息、商品的信息等。应用程序读取数据时，一般是先从缓存中读取，如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存。
2、异步方式，如果有耗时操作，可以采用异步，比如celery
3、代码优化，避免循环和判断次数太多，如果多个if else判断，优先判断最有可能先发生的情况

数据库优化：
1、如有条件，数据可以存放于redis，读取速度快
2、建立索引、外键等
"""

#58、使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
dic = {"name":"zs","age":18}
dic.pop("name")
print(dic)
dic = {"name":"zs","age":18}
del dic["name"]
print(dic)

#59、列出常见MYSQL数据存储引擎
"""
InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，因为支持事务的提交（commit）和回滚（rollback）。 
MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，那么选择MyISAM能实现处理高效率。如果应用的完整性、并发性要求比 较低，也可以使用。
MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高。如果需要很快的读写速度，对数据的安全性要求较低，可以选择MEMOEY。它对表的大小有要求，不能建立太大的表。所以，这类数据库只使用在相对较小的数据库表。
"""

#60、计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]
A = zip(("a","b","c","d","e"),(1,2,3,4,5))
A0 = dict(A)
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
print("A0",A0)
print("A:",[i for i in A])
print("A2:",A2)
print("A3:",A3)
#dict()创建字典新方法
x = dict([["name","chen"],["age",18]])
print(x)
y = dict([["name","fang"],["age",10]])
print(y)

#61、简述同源策略
"""
 同源策略需要同时满足以下三点要求： 

1）协议相同 
2）域名相同 
3）端口相同 

 http:www.test.com与https:www.test.com 不同源——协议不同 
 http:www.test.com与http:www.admin.com 不同源——域名不同 
 http:www.test.com与http:www.test.com:8081 不同源——端口不同

 只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”
 """

#62、简述cookie和session的区别
 """
 1，session 在服务器端，cookie 在客户端（浏览器）
2、session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
3、cookie安全性比session差
"""

#63、简述多线程、多进程
"""
进程：
1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制

线程：
1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，一个进程下的多个线程可以共享该进程的所有资源
2、如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃

应用：
IO密集的用多线程，在用户输入，sleep 时候，可以切换到其他线程执行，减少等待的时间
CPU密集的用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个全局解释器锁，当前运行的线程会霸占GIL，其他线程没有GIL，就不能充分利用多核CPU的优势
"""

#64、简述any()和all()方法
"""
any():只要迭代器中有一个元素为真就为真
all():迭代器中所有的判断项返回都是真，结果才为真
python中什么元素为假？
答案：（0，空字符串，空列表、空字典、空元组、None, False）
"""
bool(0)
bool("")
bool([])
bool(())
bool({})
bool(None)

#65、IOError、AttributeError、ImportError、
#IndentationError、IndexError、KeyError、
#SyntaxError、NameError分别代表什么异常
"""
IOError：输入输出异常
AttributeError：试图访问一个对象没有的属性
ImportError：无法引入模块或包，基本是路径问题
IndentationError：语法错误，代码没有正确的对齐
IndexError：下标索引超出序列边界
KeyError:试图访问你字典里不存在的键
SyntaxError:Python代码逻辑语法出错，不能执行
NameError:使用一个还未赋予对象的变量
"""

#66、python中copy和deepcopy区别

#67、列出几种魔法方法并简要介绍用途
"""
__init__:对象初始化方法
__new__:创建对象时候执行的方法，单列模式会用到
__str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
__del__:删除对象执行的方法
"""

#68、C:Users y-wu.junyaDesktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？

#69、请将[i for i in range(3)]改成生成器
a = (i for i in range(3))
type(a)

#70、a = "  hehheh  ",去除收尾空格
a = " hehheh "
a.strip()

#71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
list = [0,-1,3,-10,5,9]
list.sort(reverse = False)
print("no return value",list)

list = [0,-1,3,-10,5,9]
res = sorted(list,reverse = False)
print("return value",res)

#72、对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],
#使用lambda函数从小到大排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo,key=lambda x:x)
print(a)

#73、使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为
#[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
#（传两个条件，x<0和abs(x)）
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo,key=lambda x:(x<0,abs(x)))
print(a)

#74、列表嵌套字典的排序，分别根据年龄和姓名排序
foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
a = sorted(foo,key=lambda x:x['age'],reverse = True)
print(a)
a = sorted(foo,key=lambda x:x["name"])
print(a)

#75、列表嵌套元组，分别按字母和数字排序
foo = [(),(),]
#76、列表嵌套列表排序，年龄数字相同怎么办？

#77、根据键对字典排序（方法一，zip函数）

