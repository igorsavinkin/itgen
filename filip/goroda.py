import pickle 
file = open('cities-europe.bin','rb')
city = pickle.load(file)
city1 = []
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
city2 = []
for i in city1:
    i.upper()
    if i[0] == i[-1]:
        
        city2.append(i)
print(len(city2))
    
