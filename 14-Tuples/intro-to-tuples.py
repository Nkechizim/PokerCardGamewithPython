#a tuple is formed with the presence of a comma, 
#the paranthesis is just for readability
fruits = "avocado", "strawberry", "banana", "apple"
fruits = ("avocado", "strawberry", "banana", "apple")

print(type(fruits))
#print(dir(fruits))

#a paranthesis is necessary for an empty tuple 
beddings = ()
print(type(beddings))

mysteries = ("glorious")
print(type(mysteries))

#a one element tuple without a comma, is just a plain string or int or whatever
mysteries = ("glorious", )
print(type(mysteries))

print(tuple(["avocado", "strawberry", "banana", "apple"]))#converting a list to a tuple
print(type(tuple(["avocado", "strawberry", "banana", "apple"])))

print(tuple("abc"))
print(tuple(["abc"]))

me = ("Nkechi", "Chizim", 22, "Female", 5.5)

*name, age, gender, height = me 
print(name, age, gender, height)