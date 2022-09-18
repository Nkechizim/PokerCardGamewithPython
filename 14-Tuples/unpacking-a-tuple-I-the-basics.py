employee = ("Bob", "Sandler", "Manager", 50)

first_name = employee[0]
last_name = employee[1]
position = employee[2]
age = employee[3]

print(first_name, last_name, position, age)

#the total variables on the left must be equal to the 
# number of elements in the tuple/list, if not there'll be an error
first_name, last_name, position, age = employee

print(first_name, last_name, position, age)

employee2 = ["Bob", "Sandler", "Manager", 50]

first_name, last_name, position, age = employee2

print(first_name, last_name, position, age)

a = 5
b = 10

b, a = (a, b)
print(a, b)