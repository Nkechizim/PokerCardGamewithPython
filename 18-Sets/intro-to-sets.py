#sets are mutable, UNORDERED data structure that prohibits duplicate values. 
#It doesn't throw an error , it just deletes them
#a set can only contain IMMUTABLE data structures

stocks = {"IBM", "MSFT", "FB", "IBM", "FB"}
print(stocks)

numbers = {1, 2, 3, 4, 3, 5, 2}
print(numbers)
print(len(numbers))

lottery_numbers = {(1,2,3), (4,5,6), (1,2,3)}
print(lottery_numbers)
print(type(lottery_numbers))
print(dir(lottery_numbers))

print()

for numbers in lottery_numbers:
    for number in numbers:
        print(number)

nums = [-5, -4, -3, 3, 4, 5]

square_numbers = {num ** 2 for num in nums}
print(square_numbers)
print(len(square_numbers))