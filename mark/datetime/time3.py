import datetime
y = int(input('Введите год:'))
c = 0
for i in range(1, 13):
    a = datetime.date(y, i, 13)
    if a.weekday() == 4:
        print('Пятница 13-того найдена:', a)
        c = c + 1
print(f'В {y} году обноруженно {c} пятниц 13-того(тых)')
