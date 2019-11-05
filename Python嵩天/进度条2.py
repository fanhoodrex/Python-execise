scale=10
print("--------start--------")
for i in range(scale+1):
    a,b = '**'*i,'..'*(scale-i)
    c=(i/scale)*100
    print("{:^3.0f}% [{}->{}]".format(c,a,b))
    import time
    time.sleep(0.5)
print("over".center(70))
