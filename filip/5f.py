g = int(input())
f  = 1
while f != g :
    o = g // f
    f += 1
    print(o)
if o == 1 and o != 2 and o != 3:
    print('ПРОСТОЕ')
else:
    print ('НЕТ')
    exit()
