disney_characters = {
    "Mickey Mouse",
    "Elsa",
    "Cinderella",
    "Snow White", 
    "Donal Duck"
}

#the remove method throws an error if the element does not exist
disney_characters.remove("Elsa")
print(disney_characters)
#disney_characters.remove("Hulk")

#the remove method does not throw an error if the element does not exist
disney_characters.discard("Cinderella")
print(disney_characters)
disney_characters.discard("Hulk")
print(disney_characters)