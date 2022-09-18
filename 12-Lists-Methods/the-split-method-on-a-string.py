names = "Nkechi, Deborah, Grace, Gaberial, Glory, Chizim"
print(len(names))

#return a list of the seperated items in the string
print(names.split(", "))
print(names.split(", ", 3)) #second argument indicates the maximum times you want to split

sentence = "My name is Nkechi Deborah Chizim, I am 21 years old"
words = sentence.split(" ")
print(words)
words = sentence.split(",")
print(words)

print()

name = ["Nkechi", "Deborah", "Chizim"]

print(" ".join(name))
print("-".join(["555", "123", "789"]))
print("".join(["555", "123", "789"]))

def word_lengths(string: str):
    new_list = string.split(" ")
    index_list = []
    for elements in new_list:
        index_list.append(len(elements))
    
    return index_list

print(word_lengths("Mary Poppins was a nanny"))