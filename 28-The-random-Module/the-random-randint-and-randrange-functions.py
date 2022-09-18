import random

#returns a number between 0 and 1
print(random.random() * 100)

#the upper bound is inclusive
print(random.randint(1, 5))

#the upper bound is exclusive, the third parameter is the steps to jump by
print(random.randrange(0, 50, 10))