# Scope refers to a location in a python program in which a name can be used
# a global variable can be used in a local scope, 
# but a local variable cannot be used a global scope
age = 28

def fancy_func():
    #print(age)
    age = 100
    print(age)

fancy_func()
print(age)

TAX_RATE = 0.06

def calc_tax(price):
    return round(price * TAX_RATE, 2)

def calc_tip(price):
    return round(price * (TAX_RATE * 3), 2)

print(calc_tax(10))
print(calc_tip(10))