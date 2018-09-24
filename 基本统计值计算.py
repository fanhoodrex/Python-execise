def getnumber():
    num=[]
    inumstr=input('enter number( quit with space):')
    while inumstr !='':
        num.append(eval(inumstr))
        inumstr=input('enter number( quit with space):')
    return num

def mean(numbers):
    s=0.0
    for num in numbers:
        s+=num
    return s/len(numbers)

def dev(numbers,mean):
    sdev=0
    for num in numbers:
        sdev=sdev+(num-mean)**2
        return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med = (numbers[size//2-1]+numbers[size//2])/2
    else:
        med = (numbers[size/2])
    return med

n=getnumber()
m=mean(n)
k=dev(n,m)
z=median(n)
print('mean:{},deviation:{},median:{}'.format(m,k,z))
