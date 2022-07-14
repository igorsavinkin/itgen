i = [str(m) for m in input().split()]
for a in range(len(i) - 1):
    if i[a] == i[a]+1:
        print(i[a])
        break
else:
    print('мало слов')
