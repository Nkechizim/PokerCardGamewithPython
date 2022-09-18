people = {
    "Nkechi": [21, "Nigerian"],
    "Didi": [23, "Nigerian"],
    "Ify": [24, "Nigerian"],
    "Awy": [13, "Nigerian"],
    "Naomi": [20, "Nigerian"]
}

people["Michelle"] = [24, "American"]
print(people["Michelle"])

people["Nkechi"] = [22, "Nigerian"]
print(people)

#print(dir({}))
print()

people = {} 
people["Nkechi"] = [22, "Nigerian"]
print(people)

feelings = ["love", "happy", "sad", "sad", "love", "excited", "fear", "happy", "love"]

def count_words(feelings):
    feelings_count = {}
    for feeling in feelings:
        if feeling not in feelings_count:
            feelings_count[feeling] = feelings.count(feeling)
    return feelings_count

print(count_words(feelings))