"""print(str.__add__('1','2'))
print(int.__add__(2,3))


a = None
print(a)
class classname(object):
    pass
s=(1,2,3)
for i in range(3):
    print(s)
a,b,c=s
print("{}+{}+{} = abc".format(c,b,a))
"""
# type(None)

for i in range(1,10):
    for j in range(1,i+1):
        print( '%d X %d = %d' % (j,i,i*j),end = '  ' )
    print('  ')

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d X %d = %d' % (j,i,i*j),end = '  ') 
        j += 1
    print('')
    i += 1

