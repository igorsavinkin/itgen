a = [int(i) for i in input().split()]
n = int(input())
cl = a[0]
for i in range(1 , len(a)):
    if abs( n - a[i]) < abs(n- cl) \
       or abs( n - a[i]) == abs(n- cl) and a[i]<cl:
        cl = a[i]
print(cl)
        
