people = {
    "Nkechi": [21, "Female"],
    "Didi": 23,
    "Ify": 24,
    "Awy": 13,
    "Naomi": 20,
    "Claudia": 23
}

#the second argument in the get method 
#provides a fallback value in case the key does not exist, 
#if nothing is given it displays 'None', 
#the get method does not mutate the dictionary
print(people.get("Awy", "Not Found"))
print(people.get("Ada", "Not Found"))
print(people.get("Ada"))
print(people)

print()

#the setdefault method adds a key to the didtionary only if it does not exist
people.setdefault("Ada", [25, "Nigerian"])
print(people)
people.setdefault("Awy", "15")
print(people)
people.setdefault("Ada")
print(people)

print()
def to_dictionary(alist):
    new_dict = {}
    for position, word in enumerate(alist):
        if word not in new_dict:
            new_dict[word] = position
    return new_dict

detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
print(to_dictionary(detectives))

def length_counts(strings):
    new_dict = {}
    for word in strings:
        if len(word) not in new_dict:
            new_dict[len(word)] = 1
        else:
            new_dict[len(word)] += 1
    
    return new_dict

sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
print(length_counts(sa_countries))