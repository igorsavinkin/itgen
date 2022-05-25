with open('evens.txt', 'a') as file:
    d = 0
    for i in range(10):
          d += 2
          file.write(str(d) + ' ')
          
