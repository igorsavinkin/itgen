import random
import math  
fn = int(input('от какого числа загадать число '))
tn = int(input("до какого числа загадать число "))
d = math.ceil(math.log(tn - fn)) + 3
print('количество ваших попыток',d)
secret = random.randint(fn,tn)
a = 0
d=""
while d != secret:
    d = int(input(f'введите число: от {fn} до {tn} '))
    if d > secret :
        print('загаданое число меньше ! попробуйте ещё раз ')
    elif d < secret :
        print('загаданое число  больше ! попробуйте ещё раз ')
    else :
        print('поздравляем вы выйгграли ')
        print('количество ваших попыток :',a)
        break

    a += 1
    if a == d:
        
        print("LOZER ВЫ ПРОИГРАЛИ")
        break

