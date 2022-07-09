import turtle as t
import random
colors = ['green','yellow','blue','red','orange','purple']
t.Pen()
n = 300
t.up()
t.goto(0,-300)
t.down()
while n > 0:
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    t.circle(n)
    n = n - 5
    t.end_fill()
    
