i1 = int(input())
i2 = int(input())
i3 = int(input())
if i1 > i2 and i1 > i3:
    print(i1)
elif i1 < i2 and i2 > i3:
    print(i2)
elif i1 == i2 and i1 > i3:
    print(i2)
else:
    print(i3)
