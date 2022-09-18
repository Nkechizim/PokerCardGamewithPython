
breakfasts = ["Eggs", "Cereal", "Fruit Salad"]
lunches = ["Rice", "Pasta", "Fufu"]
dinners = ["Oats", "Peppersoup", "Custard"]

#the zip function combines lists that have something in common 
#based on their shared index position
print(zip(breakfasts, lunches, dinners))
print(type(zip(breakfasts, lunches, dinners)))
print(list(zip(breakfasts, lunches, dinners)))

print()

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners):
    print(f"My meal for the day was {breakfast}, {lunch} and {dinner}.")