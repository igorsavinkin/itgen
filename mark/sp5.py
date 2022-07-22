i = [str(m) for m in input().split()]
b = 0
for a in range(len(i) - 1):
    if i[a].isalpha() == i[a + 1].isalpha():
        print(i[a] , i[a + 1])
        b = b + 1
if b == 0:
    print('мало слов')
