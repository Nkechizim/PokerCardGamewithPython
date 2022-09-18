#returns the removed element but cannot remove more than one element
cleaning_items = ["mop", "broom", "brush", "packer", "duster", "sponge", "soap"]
print(cleaning_items)

cleaning_items.pop()
print(cleaning_items)

removed_item = cleaning_items.pop(2)
print(cleaning_items)
print(removed_item)

#doesn't return the removed element but can remove more than one element
del cleaning_items[2]
print(cleaning_items)

del cleaning_items[0:2]
print(cleaning_items)


print()

#removes the first occurence of an element from the list
cleaning_items = ["mop", "broom", "brush", "broom", "duster", "sponge", "soap", "mop"]
print(cleaning_items)

cleaning_items.remove("mop")
print(cleaning_items)

for x in cleaning_items:
    if x == "broom":
        cleaning_items.remove(x)

print(cleaning_items)

if "wop" in cleaning_items:
    cleaning_items.remove("wop")
print(cleaning_items)

cleaning_items.reverse()
print(cleaning_items)

print(sorted(cleaning_items)) #does not mutate the original list, it returns a new list
print(cleaning_items)

cleaning_items.sort() #changes the original list
print(cleaning_items)

cleaning_items.clear()
print(cleaning_items)