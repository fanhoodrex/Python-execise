try:
    guess = eval(input("number integer:"))
    print(guess**2)
except NameError:
    print('not integer')
else:
    print('\nexcellent')
finally:
    ('\nit is over')
