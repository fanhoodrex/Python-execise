fname=input('type the name of file you wanna open:')
fo=open(fname,'r')
for line in fo.readlines():
    #将所有的信息文本以行方式生成一个列表，每行是一个列表的元素
    print(line)
fo.close()
