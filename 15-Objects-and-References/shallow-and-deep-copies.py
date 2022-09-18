#using the normal methods of copying does not create a copy of the nested list, 
#so if th orignial nested list is modified the nested lost in the copy is modified too
import copy

numbers = [2, 3, 4]
a = [1, numbers, 5]

b = a[:]
b = a.copy()
b = copy.copy(a)

print(a == b)
print(a is b)
print(a[1] is b[1])

a[1].append(100)
print(b)

#creating a deep copy
c = copy.deepcopy(a)
print(a == c)
print(a is c)
print(a[1] is c[1])
a[1].append(200)
print(a)
print(b)
print(c)

web_dev = ["HTML", "CSS", "JavaScript"]

frontend = web_dev



web_dev.append("React")

print(frontend)