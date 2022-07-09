print('Введите ваш возраст:')
i = int(input())
if i >= 10:
    print('Вы уверены?')
    b = input()
    if b == 'да':
        print('доступ разрешён !')
