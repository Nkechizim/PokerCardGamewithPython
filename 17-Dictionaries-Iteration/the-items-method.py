chinese_food = {
    "Sesame Chicken": 9.99,
    "Boneless Spare Rib": 7.99,
    "Fried Rice": 1.99
}
#the items method returns a tuple
#with the first value being the key and the second value being the value
for food, price in chinese_food.items():
    print(f"The meal if {food} and the price is {price}")