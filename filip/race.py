import random
import turtle
a= turtle.Pen()
b=turtle.Pen()
a.width(5)
a.pencolor('#ffcd05')
b.pencolor('#f2050d')
b.width(5)
a.up()
b.up()
a.shape("turtle")
b.shape("turtle")
a.goto(-300,-50)
b.goto(-300,50)
b.down()
a.down()
step_a =1

while a.xcor() <= 200 and b.xcor() <= 200:
    a.forward(random.randint(0,7))
    b.forward(random.randint(0,7))
if a.xcor() < b.xcor()  :
    print("победитель краный ")
elif a.xcor() > b.xcor()  :
    print("победитель жёлтый  ")
else:
    print('ничья')
