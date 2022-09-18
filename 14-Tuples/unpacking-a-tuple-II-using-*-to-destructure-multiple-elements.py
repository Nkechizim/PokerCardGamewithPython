employee = ("Bob", "Sandler", "Manager", 50)

#you can only have one variable with an asterisk
first_name, last_name, *details = employee

print(first_name, last_name, details)

*name, position, age = employee
print(name, position, age)

first_name, *details, age = employee
print(first_name, details, age)

first_name, last_name, position, *details = employee
print(first_name, last_name, position, details)

first_name, last_name, position, details = employee
print(first_name, last_name, position, details)