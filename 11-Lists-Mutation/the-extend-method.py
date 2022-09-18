#change the list
cleaning_items = ["mop", "broom"]
print(cleaning_items)

cleaning_items.extend(["brush", "packers", "duster"])
print(cleaning_items)

cleaning_items.extend(["sponge", "soap"])
print(cleaning_items)

cleaning_items.append(["sponge", "soap"])
print(cleaning_items)

some_cleaning_items = ["mop", "broom"]
extra_cleaning_items = ["brush", "packers", "duster"]

#creates a new list
cleaning_items = some_cleaning_items + extra_cleaning_items
print(cleaning_items)
print(some_cleaning_items)
print(extra_cleaning_items)

def factors(number: int):
    number_factors = []
    for num in range(1, (number + 1)):
        if(number % num == 0):
            number_factors.append(num)
    return number_factors

print(factors(64))