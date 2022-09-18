class Store():
    def __init__(self):
        self.owner = "Nkechi"

    def exclaim(self):
        return "Lots of stuff to buy, Come Inside!!"

class CoffeeShop(Store):
    pass

starbucks = CoffeeShop()
print(starbucks.owner)
print(starbucks.exclaim())