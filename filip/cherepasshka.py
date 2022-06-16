import turtle
t=turtle.Pen()
t.up()
t.goto(-200,-200)
t.speed(1)
t.down()

while t.xcor() <200:
    t.forward(5)
    t.up()
    t.forward(5)
    t.down()
t.left(90)
while t.ycor() <200:
    t.forward(5)
    t.up()
    t.forward(5)
    t.down()    
t.left(90)
while t.xcor() > -200:
    t.forward(5)
    t.up()
    t.forward(5)
    t.down()    
t.left(90)
while t.ycor() > -200:
    t.forward(5)
    t.up()
    t.forward(5)
    t.down()    
t.left(90)
