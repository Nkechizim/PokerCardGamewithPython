nuts = "5coconut, 3walnut, 2cashew nut!"

print(nuts.capitalize())
print(nuts.upper())
print(nuts.title())
print("COCONUT".lower())
print("COCONUT".lower().title()) #method chaining using two or more methods
print("CoCoNUT".swapcase())

print()

print(nuts.islower())
print(nuts.title().istitle())
print(nuts.isupper())
print(nuts.isalpha())
print(nuts.isnumeric())
print(nuts.isalnum())

print()

print("Cashewnut".isalpha())
print("5Cashewnut".isalnum())
print("2563".isnumeric())
print("  ".isspace())