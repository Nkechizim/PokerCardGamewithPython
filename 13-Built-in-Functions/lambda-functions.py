animals = ["cats", "dogs", "rabbit", "chicken", "girrafe", "elephant"]

print(list(filter(lambda animal: len(animal) > 5, animals)))
print(list(filter(lambda animal: "a" in animal, animals)))
print()
print(list(map(lambda animal: animal.count("a"), animals)))
print(list(map(lambda animal: animal.replace("s", "$"), animals)))