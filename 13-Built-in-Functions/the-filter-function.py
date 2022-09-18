values = [3.45, 5.67, 7.89]

squares_values = [value ** 2 for value in values]
print(squares_values)
print(list(value ** 2 for value in values))

print(list(map(lambda value: value ** 2, values)))