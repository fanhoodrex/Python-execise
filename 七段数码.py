#program has buggggggggssss

import turtle ,time
def drawgap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):
    drawgap()
    turtle.pendown()if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)
    
def drawdigit(d):
    drawline(True) if d in [2,3,4,5,6,8,9]else drawline(False)
    drawline(True) if d in [0,1,3,4,5,7,8,9]else drawline(False)
    drawline(True) if d in [0,2,3,5,6,8,9]else drawline(False)
    drawline(True) if d in [0,2,6,8]else drawline(False)
    turtle.left(90)
    drawline(True) if d in [0,4,5,6,8,9]else drawline(False)
    drawline(True) if d in [0,2,3,5,6,7,8,9]else drawline(False)
    drawline(True) if d in [0,1,2,3,4,7,8,9]else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawdate(date):
    for i in date:
        drawdigit(eval(i))

def drawdate(date):
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('year',font=('Arial',18,'Normal'))
            turtle.pencolor('Green')
            turtle.fd(40)
        elif i =='=':
            turtle.write('month',font=('Arial',18,'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i =='+':
            turtle.write('day' ,font =('Arial',18,'Normal'))
        else:
            drawdigit(eval(i))

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate(time.strftime('%Y-%m=%d+,',time.gmtime()))
    turtle.speed(0.1)
    turtle.hideturtle()
    turtle.done()
    
    drawdate(datetime.datetime.now().strftime('%Y%m%d'))
    turtle.hideturtle()
main()

    
