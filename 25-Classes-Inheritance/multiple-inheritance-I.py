class FrozenFood():
    def thaw(self, minutes):
        print(f"Thawing for {minutes} minutes!")
    def store(self):
        print("Putting in the Freezer")     

class Desert():
    def add_weight(self):
        print("Wow, putting on pounds!")
    def store(self):
        print("Putting in the refrigerator")

class IceCream(Desert, FrozenFood):
    pass

ic = IceCream()
ic.thaw(5)
ic.add_weight()
ic.store()
print(IceCream.mro()) 