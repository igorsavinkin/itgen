import datetime
year = int(input('Ведите год '))
p13 = 0
for i in range(1,13):
    date = datetime.date(year, i, 13)
    if date.weekday() == 4:
        p13 += 1
        print(f' Пятница 13-того найдена: {date}')
print(f'Всего было найдено {p13} пятниц 13-того')
        
