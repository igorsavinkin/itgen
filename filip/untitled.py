y = float(input())
d = 0
d += y
while y >0:
    if y >= 1500 :
        y *= 0.92
    d += y
    print(y)
    y = float(input())
    print(d)
