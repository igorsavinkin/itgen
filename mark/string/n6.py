a = input()
s1 = a.find(' ')
w1 = a[:s1]
s2 = a.rfind(' ')
w2 = a[s1 + 1:s2]
w3 = a[s2 + 1 :]
c = w1.count('a')
if 'a'in w2:
    d = w2.replace("a", "A")
else:
    d = 'error'
print(w1)
print(w2)
print(w3)
print(c)
print(d)
print(len(w3))
