file = open('numbers.txt','w')
i = 0
while i <= 20:
    file.write(f'{i}')
    file.write(' ')
    i += 2
file.close()
