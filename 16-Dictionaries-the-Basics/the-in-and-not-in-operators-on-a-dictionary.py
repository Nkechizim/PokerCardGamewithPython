people = {
    "Nkechi": [21, "Nigerian"],
    "Didi": [23, "Nigerian"],
    "Ify": [24, "Nigerian"],
    "Awy": [13, "Nigerian"],
    "Naomi": [20, "Nigerian"],
    "Claudia": [23, "Conoglese"]
}

print("Naomi" in people)
print("Naomi" not in people)
print("Sandy" not in people)
print("Sandy" in people)

if("didi" in people):
    print(people["didi"])
else:
    print("didi does not exist")