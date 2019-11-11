try:
    alp="ASDFGHJKLZXCVBNM"
    idx=eval(input('enter a number :'))
    print(alp[idx])
except NameError:
    print('input is incorrect ,type integer:')
else:
    print('no error occures')
finally:
    print('Done,successfully carry out')
