import math

def estimated(size=1,number=None,time=None):
	if (number == None) and (time != None):
		number = math.ceil(size * 80 / time)
		print("项目大小为%.2f个标准项目，如果需要在%.2f个工时完成，则需要人力数量为:%d人"%(size,time,number))
	elif (number != None) and (time = None):
		time = number.ceil(size * 80 / number)
        print('项目大小为%.2f个标准项目，使用%.2f个人力完成，则需要工时数量为：%d个' %(size,number,time))  

choice = int(input("请选择计算类型：（1-人力计算，2-工时计算"))
if choice == '1':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    time = float(input('请输入工时数量：（可以输入小数）'))
    estimated(size,number,time)

elif choice == '2':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = int(input('请输入人力数量：（请输入整数）'))
    estimated(size,number,time)


punches = ['石头','剪刀','布']
elif user_choice == punches[punches.index(computer_choice)-1]:

if user_choice = "石头" 
computer_choice = "剪刀" 
punches.index(user_choice) = 0 
punches.index(computer_choice) = 1
punches.index(computer_choice) - 1 = 0  
punches[punches.index(computer_choice)-1] = "石头"


if user_choice = "剪刀"
computer_choice = "布" 
punches.index(user_choice) = 1
punches.index(computer_choice) = 2
punches.index(computer_choice) - 1 =  1 
punches[punches.index(computer_choice)-1] = "剪刀"

if user_choice = "布"
computer_choice = "石头"
punches.index(user_choice) = 2
punches.index(computer_choice) = 0
punches.index(computer_choice) - 1 = -1 
punches[punches.index(computer_choice)-1] = "布"

print('\n欢迎使用除法计算器！\n')

while True:
    try:
        x = input('请你输入被除数：')
        y = input('请你输入除数：')
        z = float(x)/float(y)
        print(x,'/',y,'=',z)
        break  # 默认每次只计算一次，所以在这里写了 break。
    except ZeroDivisionError:  # 当除数为0时，跳出提示，重新输入。
        print('0是不能做除数的！')
    except ValueError:  # 当除数或被除数中有一个无法转换成浮点数时，跳出提示，重新输入。
        print('除数和被除数都应该是整值或浮点数！')
    
    # 方式2：将两个（或多个）异常放在一起，只要触发其中一个，就执行所包含的代码。
    # except(ZeroDivisionError,ValueError):
    #     print('你的输入有误，请重新输入！')
    
    # 方式3：常规错误的基类，假设不想提供很精细的提示，可以用这个语句响应常规错误。
    # except Exception:
    #     print('你的输入有误，请重新输入！')
    
    i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d X %d = %d' % (j,i,i*j),end = '  ') 
        j += 1
    print('')
    i += 1

for i in range(1,10):
    for j in range(1,i+1):
        print( '%d X %d = %d' % (j,i,i*j),end = '  ' )
    print('  ')

text= "A,B,C"
l=text.split(",")
print(l)

a = []
for i in 'ABC':
    print(i)
    a.append(i)
print(a)

movie = {
    '妖猫传':['黄轩','染谷将太'],
    '无问西东':['章子怡','王力宏','祖峰'],
    '超时空同居':['雷佳音','佟丽娅']
}
name=input('你查询的演员是？:')
for i in movie:
    print(i)
    # actors=[i]
    # if name in actors:
    #     print(name+'出演了'+i)

import math

def estimated(size=1,number=None,time=None):
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))  
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  

choice = input('    ')
if choice == '2':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = int(input('请输入人力数量：（请输入整数）'))
    time = None
    estimated(size,number,time)
elif choice == '1':
    size = float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
    number = None
    time = float(input('请输入工时数量：（可以输入小数）'))
    estimated(size,number,time)


# 类的创建使用 > 图书馆管理系统
class Book:
 
    def __init__(self, name, author, comment, state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state
 
    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)
 
class BookManager:

    books = []
    def __init__(self):
        book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。',1)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)
 
    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            else:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
                break
 
    def show_all_book(self):
        print('书籍信息如下：')
        for book in self.books:
            print(book)
            print('')

    def add_book(self):
        new_name = input('请输入书籍名称：')
        new_author =  input('请输入作者名称：')
        new_comment = input('请输入书籍推荐语：')
        new_book = Book(new_name, new_author, new_comment)
        self.books.append(new_book)
        print('书籍录入成功！\n')

    def check_book(self,name):
        for book in self.books:
            if book.name == name:
                 return book 
        else:
            return None

    def lend_book(self):
        name = input('请输入书籍的名称：')
        res = self.check_book(name)

        if res != None:
            if res.state == 1:
                print('你来晚了一步，这本书已经被借走了噢')
            else:
                print('借阅成功，借了不看会变胖噢～')
                res.state = 1
        else:
            print('这本书暂时没有收录在系统里呢')
    
    def return_book(self):
        name = input('请输入归还书籍的名称：')
        res = self.check_book(name)
        if res == None:
            print('没有这本书噢，你恐怕输错了书名～')
        else:
            if res.state == 0:
                print('这本书没有被借走，在等待有缘人的垂青呢！')
            else:
                print('归还成功！')
                res.state = 0
 
manager = BookManager()
manager.menu()

import csv

with open('test.csv',,newline = '', encoding = 'utf-8')  as f:
    #参数encoding = 'utf-8'防止出现乱码
    content = csv.reader(f)
    for row in content:
        print(row)