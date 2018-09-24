import turtle as t
t.title('automatic draw')
t.setup(800,600,0,0)
t.pencolor('red')
t.pensize(5)
#read data
datals=[]
f=open('date.txt','w+')

for line in f:
    line = line.replace('\n','')
    datals.append(list(map(eval,line.split(','))))
f.close()
#read data
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
