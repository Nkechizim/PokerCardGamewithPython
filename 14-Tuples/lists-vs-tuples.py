birthday = (27, 5, 1998)

print(len(birthday))

print(birthday[0])
print(birthday[1])
print(birthday[2])
#print(birthday[3])

print(birthday[-1])

numbers = [(45, 78, 56), (23, 45, 78)]
print(numbers)
print(type(numbers))
print(type(numbers[0]))

numbers2 = (
    [45, 88, 56], 
    [13, 25, 78]
)

print(numbers2)
print(type(numbers2))
print(type(numbers2[0]))

numbers2[0][2] = 987
numbers2[1].append(65)
print(numbers2)