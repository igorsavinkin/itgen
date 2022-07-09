capitals = ['Москва' ,'лондон' ,'Берлин' ,'Хельсенки']
e = input()
capitals.append(e)
for i in range(len(capitals)):
    if len(capitals[i]) < 6 :
        capitals.remove(capitals[i])
print(*capitals)
