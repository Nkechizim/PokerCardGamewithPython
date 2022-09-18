import copy

students = ["Tais", "Thiri", "Aya", "Dina"]
athletes = students
nerds = ["Tais", "Thiri", "Aya", "Dina"]

print(students == athletes)
print(athletes == nerds)
print(students == nerds)

print(students is athletes)
print(students is nerds)

a = 56
b = 56

print(a == b)
print(a is b)

print()
#creating a shallow copy, works well the list doesn't contain a nested list
a = [1, 2, 3]
b = a[:]

print(a == b)
print(a is b)

c = a.copy()
print(a == c)
print(a is c)

d = copy.copy(a)
print(a == d)
print(a is d)