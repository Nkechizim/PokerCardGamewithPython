def delete_all(strings_list: list, target: str):
    new_string = []
    for string in strings_list:
        if string != target:
            new_string.append(string)
    return new_string

print(delete_all([1, 3, 5, 3], 3))
print(delete_all([4, 4, 4, 6], 4))
print(delete_all([4, 4, 4, 4, 5], 4))

def push_or_pop(numbers):
    new_numbers = []

    for number in numbers:
        if number >= 5:
            new_numbers.append(number)
        else:
            new_numbers.pop()
    
    return new_numbers

print(push_or_pop([10, 20, 2, 30]))
print(push_or_pop([10, 4]))
print(push_or_pop([10, 20, 30]))
print(push_or_pop([10]))