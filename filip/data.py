import datetime

me = int(input('Введите месяц рождения '))
g = int(input('Введите год рождения '))
d = int(input('Введите день рождения '))
h = int(input('Введите часы рождения '))
mi = int(input('Введите минуты  рождения '))
s = int(input('Введите секунды рождения '))
mil = int(input('Введите милисекунды рождения '))

a = datetime.datetime(g,me,d,h,mi,s,mil)
d = datetime.datetime.now()
m = d-a
m1 = m.days * 24*60*60*1000000
m4 = m.seconds *1000000
m5 = m.microseconds
milisecond = m5 + m4  + m1
print(milisecond)
