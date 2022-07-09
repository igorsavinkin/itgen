s = int(input())
p = s
for i in range(5):
    if s == 0:
        p = p
    else:
        p = p * s
    s = int(input())
print(p)
