import turtle as t
t.Pen()
t.up()
t.goto(-250,-250)
t.down()
while t.xcor() < 200 or t.ycor() < 200:
    t.fd(20)
    t.lt(90)
    t.fd(20)
    t.rt(90)
