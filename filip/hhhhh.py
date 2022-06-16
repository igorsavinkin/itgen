import turtle
import random

t = turtle.Pen()
t.speed(5)

r = 100
while r >= 20:
    t.pencolor(random.random(),random.random(),random.random())
    t.fillcolor(random.random(),random.random(),random.random())
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    r -= 10
    t.down()
    
