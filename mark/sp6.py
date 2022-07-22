i = [int(m) for m in input().split()]
n = int(input())
c = i[0]
for k in i:
    if abs(n - k) < abs(n - c) or abs(n - k) == abs(n - c) and k < c:
        c = k
print(c)
