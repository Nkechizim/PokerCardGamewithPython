def nested_sum(num_lists):
    sum = 0
    for lists in num_lists:
        for num in lists:
            sum += num
    
    return sum

print(nested_sum([[1, 2, 3], [4, 5]]))
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))