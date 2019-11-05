import math
def getnum():
    nums=[]
    inumstr=input('Enter number(Quit with space click):')
    while inumstr!='':
        nums.append(eval(inumstr))
        inumstr = input('Enter number(exit with space click):')
    return nums
def mean(numbers):
    s=0
    for num in numbers:
        s+=num
    return s/len(numbers)

def dev(numbers,mean):
    sdev=0
    for num in numbers:
        sdev+=sedv(num-mean)**2
    return sqrt(sdev/(len(numbers)-1))

def median(numbers):
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
    return med
n = getnum()
m = mean(n)
print('mean={}, standard deviation={}, median={}'.format(m,\
                                dev(n,m),median(n)))
