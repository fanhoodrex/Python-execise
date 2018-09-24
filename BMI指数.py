#5.2calBMI.py
height,weight=eval(input("enter height and weight\
()[]:"))
bmi=weight/pow(height,2)
print("BMI value :{:.2f}".format(bmi))
who,dom='',''
if bmi < 18.5:
    who,dom='thin','thin'
elif 18.5 <=bmi<24:
    who,dom='normal','normal'
elif 24 <= bmi<25:
    who,dom = 'normal','chubby'
elif 25<=bmi<28:
    who,dom='chubby','chubby'
elif 28<=bmi<30:
    who,dom='chubby','fat'
else:
    who,dom='fat','fat'
print('BMI index is: international{0}, domestic{1}'.format(who,dom))
