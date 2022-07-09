i = input()
k = i.find(' ')
i1 = i[0:k]
i2 = i[k:]
if len(i1)> len(i2):
    print(i1, i2)
else:
    print(i2, i1)
