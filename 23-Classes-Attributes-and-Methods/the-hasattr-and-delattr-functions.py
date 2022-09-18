stats = {
    "name": "BBQ Chicken",
    "price": 19.99,#
    "size": "Extra-Large",
    "ingredients": ["Chicken", "Onions", "BBQ Sauce"]
}

class Pizza():
    def __init__(self, stats):
        for attribute, value in stats.items():
            setattr(self, attribute, value)

pizza1 = Pizza(stats)
print(pizza1.size)
print(pizza1.ingredients)

stats_to_delete = ["size", "diameter", "spiciness", "ingredients"]
for stat in stats_to_delete:
    if hasattr(pizza1, stat):
        delattr(pizza1, stat)

#print(pizza1.size)
#print(pizza1.ingredients) 

class Coffee():
    def __init__(self, cream, sugar, half_and_half):
        self.cream = cream
        self.sugar = sugar
        self.half_and_half = half_and_half
 
morning_joe = Coffee(True, False, True)
 
for val in ["cream", 
            "pumpkin spice", 
            "cinnamon", 
            "sugar", 
            "half_and_half"]:
    if hasattr(morning_joe, val):
        setattr(morning_joe, val, not getattr(morning_joe, val))
 
print(morning_joe.cream, morning_joe.sugar, morning_joe.half_and_half)