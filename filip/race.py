import random
import turtle
a= turtle.Pen()
b=turtle.Pen()
c=turtle.Pen()
a.width(5)
c.width(5)
c.up()
c.pencolor('#45F911')
c.goto(296,180)
c.down()
c.goto(296,-100)
a.pencolor('#ffcd05')
b.pencolor('#f2050d')
c.pencolor('#0D19EA')
b.width(5)

a.up()
b.up()
c.up()
a.shape("turtle")
b.shape("turtle")
c.shape("turtle")
a.goto(-300,-50)
b.goto(-300,50)
c.goto(-300,130)
b.down()
a.down()
c.down()
step_a = 1
step_b = 1
step_c = 1
while a.xcor() <= 300 and b.xcor() <= 300 and c.xcor() <= 300 :
    if random.randint(0,1) == 0 and step_a <7:
        step_a += 1
    elif step_a > 1:
        step_a-=1
    if random.randint(0,1) == 0 and step_b <7:
        step_b += 1
    elif step_b > 1:
        step_b-=1
    if random.randint(0,1) == 0 and step_c <7:
        step_c += 1
    elif step_c > 1:
        step_c-=1
    a.forward(step_a)
    b.forward(step_b)
    c.forward(step_c)

if a.xcor() < b.xcor() and b.xcor() > c.xcor() :
    print("победитель краный ")
    a.ht()
    c.ht()
elif  a.xcor() > c.xcor() :
    b.ht()
    c.ht()
    print("победитель жёлтый  ")
elif c.xcor() > b.xcor()  :
    print('победитель синий')
    b.ht()
    a.ht()
else:
    print('ничья')
