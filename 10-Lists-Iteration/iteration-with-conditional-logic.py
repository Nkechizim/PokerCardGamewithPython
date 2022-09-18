values = [3, 5, 4, 13, 23, 12, 7, 8, 16, 24, 23, 21]
values2 = [5, 10, 15, 20, 25]


def sum_of_odds(numbers: list):
    total = 0
    for num in numbers:
        if(num % 2 != 0):
            total += num
    return total

def greatest_num(numbers: list):
    greatest = 0
    for num in numbers:
        if(num > greatest):
            greatest = num
    return greatest

print(sum_of_odds(values))
print(sum_of_odds(values2))

print(greatest_num(values))
print(greatest_num(values2))
