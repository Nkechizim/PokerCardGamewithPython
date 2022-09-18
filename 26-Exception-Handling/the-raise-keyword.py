def add_positive_numbers(a, b):
    try:
        if (a <= 0 or b <= 0):
            raise ValueError("Both numbers must be positive and greater than 0")

        return a + b
    
    except ValueError as e:
        return f"Caught ValueError: {e}"

print(add_positive_numbers(8, 9))
print(add_positive_numbers(8, -9))
print(add_positive_numbers(0, -9))