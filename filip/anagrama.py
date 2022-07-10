import random
a = ['машина','вертолёт','самолёт','корабль']
r = random.choice(a)
letters = [i for  i in r]
e = ''
while e != r:
    
    random.shuffle(letters)
    print(letters)
    e = input('введите правильное слово : ')
print('вы правильно угадали слово')
