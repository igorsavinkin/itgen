file = open('pangrams.txt', encoding = 'UTF-8')
text1 = file.read()
file.close()
print(text1.replace('\n', ' '))
