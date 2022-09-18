cleaning_items = ["mop", "broom", "brush", "broom", "broom", "sponge", "soap", "mop"]

print(cleaning_items.count("broom"))
print(cleaning_items.index("broom")) #returns the index position of the first occurence

if "packers" in cleaning_items:
    print(cleaning_items.index("packers")) #throws an error if the element is not in the list

print()
#second parameter is the starting index which is inclusive
print(cleaning_items.index("mop", 2)) 

print()

hours_of_sleep = [7.0, 7.6, 8.0, 7.0, 8.3, 7.0]

print(hours_of_sleep.count(6.0))
print(hours_of_sleep.count(7.0))
print(hours_of_sleep.count(7))
print(hours_of_sleep.index(7))

def encrypt_message(string: str):
    alphabets = "abcdefghijklmnopqrstuvwxyzab"
    new_string = ""
    
    for letter in string:
        new_string += alphabets[alphabets.index(letter) + 2]
    
    return new_string

print(encrypt_message("xyz"))