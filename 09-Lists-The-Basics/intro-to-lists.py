# Create a list with a single Boolean — True — and assign it to the variable "active".
active = [True]

# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".
favorite_numbers = [5, 89, 78, 41, 63]

# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".
colors = ["red", "green", "blue"]
print(colors[2][3])

# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise
def is_long(meals: list, object):
    print(object in meals)
    print(object not in meals)
    return True if(len(meals) > 5) else False

print(is_long(["breakfast", "lunch", "dinner"], 67))