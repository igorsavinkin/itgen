import time
import random
messages = ["Не буди лихо, пока оно тихо.", "Друг познается в беде.", "В тихом омуте черти водятся.", "В гостях хорошо, а дома лучше."]
print('проверка скорости набора текста.Введите следущую фразу.Я засеку время...')
time.sleep(2)
print('На старт...')
time.sleep(1)
print('Внимание...')
time.sleep(1)
print('Начали!')
a = random.choice(messages)
print(a)
start_time = time.time()
end_time = time.time()
user_time = end_time - start_time
