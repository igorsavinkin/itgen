a = input()
c = 0
for i in range(len(a) - 3):
    if a[i] == a[i + 1] and a[i] == a[i + 2]:
        c += 1
print(c)
