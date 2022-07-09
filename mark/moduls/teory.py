import random
print(random.randint(1,10))
print(random.choice([12, 8, 9, 64, -0.82, 0]))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = random.shuffle(numbers)
print(numbers)
print(new_numbers)
print(random.uniform(1, 6))
