#the find method starts searching from the left, 
#while the rfind method starts searching from the right
nuts = "5coconut, 3walnut, 2cashew nut!"
print(nuts.find("nuts")) #this would return -1
print(nuts.index("nut")) #this would return 5
print(nuts.rfind("nut")) #this would return 27

print()

print(nuts.startswith("5co"))
print(nuts.startswith("Coco"))

print()

print(nuts.endswith("ut!"))
print(nuts.endswith("Nut"))

print()

#returns the number of occurences of a substring within a string
print(nuts.count("nut"))
print(nuts.count("w"))
print(nuts.count("we"))