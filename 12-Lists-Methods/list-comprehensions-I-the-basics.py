numbers = [5, 7, 9, 10, 16]
squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
print(number)

#different method
new_squares = [num ** 2 for num in numbers]

print(new_squares)
#print (num)

items = ["purse", "table", "bed"]

items_length = [len(item) for item in items]
print(items_length)