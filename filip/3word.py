r = input()
h = r.find(' ')
word1 = r[0 : h]
print(word1.count('a'))
h2 = r.rfind(' ')
word2 = r[h+1:h2]
print(word2.replace('a','A'))
word3 = r[h2+1:]
print(len(word3))
