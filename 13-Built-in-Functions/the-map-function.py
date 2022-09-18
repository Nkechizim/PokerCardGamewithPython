numbers = [4, 8, 9, 12, 15]
cubes = [number ** 3 for number in numbers]
print (cubes)

def cube(number):
    return number ** 3

print(map(cube, numbers))
print(list(map(cube, numbers))) 

animals = ["cats", "dogs", "rabbit", "chicken", "girrafe", "elephant"]
animals_length = [len(animal) for animal in animals]
print(animals_length)

print(list(map(len, animals)))

animals_len = [animal for animal in animals if len(animal) > 5]
print(animals_len)

def animal_len(animal):
    return True if len(animal) > 5 else False

print(filter(animal_len, animals))
print(list(filter(animal_len, animals)))