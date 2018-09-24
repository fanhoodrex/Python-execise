for s in'PYTHON':
    if s=='T':
        continue
    import time
    time.sleep(1)
    print(s,end='')
else:
    time.sleep(2)
    print(' \nquit successfully')
    
