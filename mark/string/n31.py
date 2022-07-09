i = input()
i1 = i.count('{')
i2 = i.count('}')
i3 = i.count('[')
i4 = i.count(']')
i5 = i.count(')')
i6 = i.count('(')
if i1 == i2 and i3 == i4 and i5 == i6:
    print('yes')
else:
    print('no')
