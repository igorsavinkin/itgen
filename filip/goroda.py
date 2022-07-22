import pickle 
file = open('cities-europe.bin','rb')
city = pickle.load(file)
city1 = []
city2 = []
city3 = []
city4 = []
len_ = len(city)
print(len_)
file.close()
for i in city:
    m = 0
    for k in i:
        if k.isupper():
            m+=1
    if m == 1 :
        city1.append(i)
print(len(city1))

for i in city1:
    p = i.upper()
    if p[0] == p[-1]:
        
        city2.append(i)
print(len(city2))

for i in city2:
    p = i.upper()
    if p[1] == p[-2] and p[1] in 'EYUIOA':
        city3.append(i)
        
print(len(city3))
for i in city3:
    p = i.upper()
    if  'W' in p:
        city4.append(i)
h = 1000        
print(len(city4))
print(city4)
for i in city4:
    p = len(i)
    if p <= h:
        h = p
        k = i
        
print(k)
file1 = open('letter.pickle','wb')
pickle.dump(k , file1)
file1.close()


