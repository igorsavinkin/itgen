import turtle
t = turtle.Pen()
t.fillcolor("#bfbbb2")
i = int(input())
h=1
while h <= i:
    t.begin_fill()
    t.forward(20)
    t.left(90)
    t.forward(80)
    t.left(45)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(45)
    t.forward(80)
    t.left(90)
    t.forward(37)
    t.end_fill()
    h += 1

