a = input()
f = 0 
for i in range(len(a)-1):
    g = a.count(a[i])
    if g > f:
        f = g
        d = a[i]

print(f,d)
