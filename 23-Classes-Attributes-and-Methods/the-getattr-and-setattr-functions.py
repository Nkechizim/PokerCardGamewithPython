stats = {
    "name": "BBQ Chicken",
    "price": 19.99,
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

for attr in ["price", "name", "diameter", "discount"]:
    print(getattr(pizza1, attr, "Unknown"))