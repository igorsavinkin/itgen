i = input()
i1 = input()
i1.split()
k1 = i1[0]
k2 = i1[-1]
f1 = i.find(k1)
f2 = i.find(k2)
if f1 > f2:
    print(k2)
else:
    print(k1)
