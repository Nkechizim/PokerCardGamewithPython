people = {
    "Nkechi": [21, "Female"],
    "Didi": 23,
    "Ify": 24,
    "Awy": 13,
    "Naomi": 20,
    "Claudia": 23
}

#accesing adictionary by just the key value,
# without the get method, the program crashes if the key does not exist
print(people["Didi"])
print(people["Naomi"])
#print(people["naomi"])

#the second argument in the get method 
#provides a fallback value in case the key does not exist
print(people.get("Awy", "Not Found"))
print(people.get("Ada", "Not Found"))
print(people.get("Ada"))