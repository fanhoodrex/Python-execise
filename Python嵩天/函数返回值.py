def fact (n,m=1):
    s=1
    for i in range(1,n+1):
        s*=i
        return s//m,n,m
fact(10,5)
a,c=fact(10,5)
print(a,b,c)
