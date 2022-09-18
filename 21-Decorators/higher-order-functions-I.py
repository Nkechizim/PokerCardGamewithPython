#Higher Order Functions are functions that either accepts a function 
# as an argument or returns a function as a return value

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(func, a, b):
    return func(a, b)

print(calculate(add, 8, 7))
print(calculate(subtract, 8, 7))