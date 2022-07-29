import datetime
g = int(input('Введите год рождения:'))
m = int(input('Введите месяц рождения:'))
d = int(input('Введите день рождения:'))
a = datetime.date.today()
b = datetime.date(g, m, d)
c = a - b
print(f'От дня рождения до сегодня прошло {c.days} дней')
