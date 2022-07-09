import turtle 
import random
a = turtle.Pen()
b = turtle.Pen()
c = turtle.Pen()
d = turtle.Pen()
a.up()
b.up()
c.up()
d.up()
d.goto(200,-200)
d.down()
d.lt(90)
d.fd(300)
a.goto(-300,50)
b.goto(-300,-50)
c.goto(-300,-150)
a.pencolor('green')
b.pencolor('red')
c.pencolor('blue')
step_a = 1
step_b = 1
step_c = 1
c.down()
a.down()
b.down()
while a.xcor() < 200 or b.xcor() < 200:
    if random.randint(0, 1) == 1 and step_a < 7:  
        step_a += 1  
    elif step_a > 1:  
        step_a -= 1
    if random.randint(0, 1) == 1 and step_b < 7:  
        step_b += 1  
    elif step_b > 1:  
        step_b -= 1
    if random.randint(0, 1) == 1 and step_c < 7:  
        step_c += 1  
    elif step_c > 1:  
        step_c -= 1
    c.fd(step_c)
    a.fd(step_a)
    b.fd(step_b)
if c.xcor() < a.xcor() > b.xcor():
    b.ht()
    c.ht()
elif a.xcor() < b.xcor() > c.xcor():
    a.ht()
    c.ht()
elif a.xcor() < c.xcor() > b.xcor():
    a.ht()
    b.ht()
else:
    print('ничья')



