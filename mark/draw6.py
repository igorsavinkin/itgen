import turtle as t
t.Pen()
t.up()
t.goto(-200,0)
t.down()
while t.xcor() < 200:
    t.fd(10)
    t.up()
    t.fd(10)
    t.down()
