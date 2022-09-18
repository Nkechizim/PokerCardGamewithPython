disney_characters = {
    "Mickey Mouse",
    "Elsa",
    "Cinderlla"
}
print(disney_characters)
#adds only one item at a time
disney_characters.add("Ariel")
print(disney_characters)

disney_characters.add("Elsa")
print(disney_characters)

#the update methods takes more than one element at a time in form of a list of tuple
disney_characters.update(["Snow White", "Donal Duck"])
print(disney_characters)

disney_characters.update(("Beauty", "Simba", "Mickey Mouse"))
print(disney_characters)
