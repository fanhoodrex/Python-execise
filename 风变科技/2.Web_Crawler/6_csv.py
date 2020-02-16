import csv
csv_file = open("demo.csv",'w',newline='',encoding='utf-8')
#调用open()函数打开csv文件，传入参数：文件名“demo.csv”、写入模式“w”、newline=''、encoding='utf-8'。
writer = csv.writer(csv_file) #创建写对象 create object for write
writer.writerow(['电影','豆瓣评分'])
#借助writerow()函数可以在csv文件里写入一行文字 "电影"和“豆瓣评分”
writer.writerow(['银河护卫队','8.0'])
writer.writerow(['复仇者联盟','8.1'])
reader = csv.reader(csv_file) #创建读文件对象 create object for read
for row in reader:
    print(row)
csv_file.close()



