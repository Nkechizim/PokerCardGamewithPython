chinese_food = {
    "Sesame Chicken": 9.99,
    "Boneless Spare Rib": 7.99,
    "Fried Rice": 1.99
}

#the sorted method doesn't mutate the dict and it only sorts the keys 
#expect if the values method is specifically called
print(sorted(chinese_food))
print(sorted(chinese_food.keys()))
print(sorted(chinese_food.values()))
print(chinese_food)