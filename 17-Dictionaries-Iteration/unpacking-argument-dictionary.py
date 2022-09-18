def height_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0254

stats = {
    "feet": 5,
    "inches": 11
}

#the total number of key-value pairs must be equal to the number of arguments required, a
#and the keys must have the same name as the arguments required
print(height_to_meters(5, 11))
print(height_to_meters(**stats))