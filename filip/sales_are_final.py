f = 0
d = int(input('введите цену '))
if d > 1499:
        d * 0,92
        
f += d
while d >= 0:
    d = int(input('введите цену '))
    if d >= 1499:
        d * 0,92
        f += d

print(f)
