from random import choice as ch
print('Введите ваши чувства:')
s = input()
if  "не " in s or '?'in s:
    print("будем держать связь")
elif 'прекрасн' in s or "отлич" in s or 'хорош'in s:
    print(ch(["Идеально у меня тоже хорошо ",'так держать','я рад за тебя']))
elif 'плох' in s or "ужасно" in s :
    print(ch(["Не беспокойся всё наладится ",'я тоже печален']))
else:
    print("будем держать связь")
