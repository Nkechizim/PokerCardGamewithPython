def divide_by_zero(num):
    try:
        calc = 5 / num
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except TypeError as e:
        return f"Please provide a number! {e}"
    
    return calc

print(divide_by_zero(0))
print(divide_by_zero(10))
print(divide_by_zero("Hehehe"))

print()

def divide_by_zero(num):
    try:
        calc = 5 / num
    except (ZeroDivisionError, TypeError) as e:
        return f"Something went wrong! {e}"
    
    return calc

print(divide_by_zero(0))
print(divide_by_zero(10))
print(divide_by_zero("Hehehe"))