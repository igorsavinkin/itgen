import random
a = 'qwertyuiopasdfghjklzxcvbnm'
a1 = ''
a1 += random.choice(a)
a1 += str(random.randint(0,9))
a1 += random.choice(a)
a1 += str(random.randint(0,9))
a1 += random.choice(a)
a1 += str(random.randint(0,9))
a1 += random.choice(a)
a1 += str(random.randint(0,9))
a1 += random.choice(a)
a1 += str(random.randint(0,9))
print(a1)
