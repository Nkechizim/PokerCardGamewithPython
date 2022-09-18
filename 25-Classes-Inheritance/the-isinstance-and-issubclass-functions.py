print(isinstance(1, int))
print(isinstance([], int))
print(isinstance([], object))
print(isinstance(str, object))
print(isinstance(max, object))

class Person():
    pass

class Superhero(Person):
    pass

arnold = Person()
Nk = Superhero()

print(isinstance(Nk, Superhero))
print(isinstance(Nk, Person))
print(isinstance(arnold, Person))
print(isinstance(arnold, Superhero))

print(issubclass(Superhero, Person))
print(issubclass(Person, Superhero))
print(issubclass(Person, object))
print(issubclass(Superhero, object))