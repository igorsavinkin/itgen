s = int(input())
l = 2
t = 3
d = 5
if s%2==0 and s%3==0 and s%5==0:
    print(l,t,d)
elif s%2==0 and s%3==0:
    print(l,t)
elif s%2==0:
    print(l)
else:
    print('0')
