a = input().split()
r = 0
for i in range(len(a)-1):
    if a[i].isalpha() == True and a[i+1].isalpha() == True:
        print(a[i],a[i+1])
        r += 1
        
if r == 0:
    print('МАЛО CЛОВ')
