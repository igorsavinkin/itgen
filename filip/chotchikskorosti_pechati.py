import random
import time
print('Проверка скорости набора текста.Я засеку время…')
time.sleep(2)
print('На старт...')
time.sleep(1)
print('Внимание...')
time.sleep(1)
print('Начали!')
r = random.choice(['Не буди лихо, пока оно тихо.',
"Друг познается в беде.",
"В тихом омуте черти водятся.",
"В гостях хорошо, а дома лучше."])
print(r)
start_time = time.time()
y = input()
end_time = time.time()
user_time = end_time - start_time
print(f'вы ввели {round(len(y),3)} символов за {round(user_time,3)} секунд ')
print(f'Это {round(len(y) / user_time,3)} cимволов в секунду')
if y != r:
    print('у вас были ошибки')

