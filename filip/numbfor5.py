r = input()
h=r.rfind('a')
for i in range(len(r)):
    print(r[i])
    if i == h:
        break
