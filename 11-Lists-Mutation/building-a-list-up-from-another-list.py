powerball_numbers =[5, 7, 12, 24, 64]

def squares(numbers):
    squared_numbers = []

    for number in numbers:
        squared_numbers.append(number ** 2)
    return squared_numbers

print(squares(powerball_numbers))

def convert_to_float(numbers):
    float_numbers = []

    for number in numbers:
        float_numbers.append(float(number))
    return float_numbers

print(convert_to_float(powerball_numbers))

def even_or_odd(numbers):
    bool_even_odd = []

    for number in numbers:
        bool_even_odd.append(number % 2 == 0)
    return bool_even_odd

print(even_or_odd(powerball_numbers))

def only_evens(numbers):
    even_numbers = []

    for number in numbers:
        if(number % 2 == 0):
            even_numbers.append(number)
    return even_numbers

print(only_evens([4, 8, 15, 16, 23, 42]))
print(only_evens([1, 3, 5]))

def long_strings(words):
    long_words = []
    for word in words:
        if(len(word) >= 5):
            long_words.append(word)
    return long_words

print(long_strings(["Hello", "Goodbye", "Sam"]))