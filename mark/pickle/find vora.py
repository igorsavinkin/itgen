import pickle

with open('cities-europe (1).bin', 'rb') as file:
    c_e = pickle.load(file)
print(len(c_e))
c_e2 = []
for c in c_e:
    v = 0
    for i in c:
        if i.isupper():
            v += 1
    if v == 1:
        c_e2.append(c)
c_e3 = []
print(len(c_e2))
for w in c_e2:
    g = w.lower()
    if g[0] == g[-1]:
        c_e3.append(w)
print(len(c_e3))
c_e4 = []
for z in c_e3:
    x = z.lower()
    if x[1] in 'aeiouy' and x[1] == x[-2]:
        c_e4.append(z)
print(len(c_e4),c_e4)
c_e5 = []
for i in c_e4:
    for s in range(len(i)):
        if i[s] == 'w':
            c_e5.append(i)
            break
print(len(c_e5),c_e5)
a = min(c_e5, key=len)
with open('glupi vorisko.bin', 'wb') as file:
    pickle.dump(a,file)
    
            
