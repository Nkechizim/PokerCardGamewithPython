print("nkechini".find("n"))

def sum_of_values_and_indices(numbers):
    total = 0
    for index, num in enumerate(numbers):
        total += (index + num)
    return total

print(sum_of_values_and_indices([1, 2, 3]))