#an instance method is a function that belongs to an object

class Pokemon():
    def __init__(self, name, specialty, health = 100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def describe(self):
        return f"I am {self.name}, and I am a {self.specialty} pokemon"

    def take_damage(self, amount):
        self.health -= amount

squirtle = Pokemon("Squirtel", "Water")
charmander = Pokemon("Charmander", "Fire", health=110)
print(squirtle.describe())
charmander.describe()

print(squirtle.health)
squirtle.take_damage(30)
print(squirtle.health)

print(charmander.health)