a = 0
i = 0
while i >= 0:
    i = float(input())
    if i > 1500:
        i = i - (i / 100 * 8 )
    a = a + i
c =  a - i  
print(c)
