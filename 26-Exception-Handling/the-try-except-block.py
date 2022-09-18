def divide_by_zero(num):
    try:
        calc = 5 / num
    except:
        calc = 0
    
    return calc

print(divide_by_zero(0))
print(divide_by_zero(10))
print(divide_by_zero("Hehehe"))