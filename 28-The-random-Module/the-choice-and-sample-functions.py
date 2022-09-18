from random import random, randrange, choice

print(random.choice(["Didi", "Awy", "Nk", "Ify"]))
print(random.choice((1, 2, 4, 6, 7)))
print(random.choice("Beautiful"))
#print(random.choice([]))

lottery_numbers = [random.randint(1, 50) for value in range(50)]
print(lottery_numbers)

print(random.sample(lottery_numbers, 1))
print(random.sample(lottery_numbers, 3))
print(random.sample(lottery_numbers, 6))

import random

roles = ["DPS", "Tank", "Healer"]

random.shuffle(sorted(roles))

print(roles) # ["DPS", "Tank", "Healer"]