a = [int(i) for i in input().split()]
res = 'YES'
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        res = 'NO'
        break
print(res)
