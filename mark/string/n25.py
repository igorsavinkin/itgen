i = input()
aw = i.find('a')
bw = i.find('b')
if aw > bw:
    print('b')
elif aw < bw:
    print('a')
else:
    print('error')
