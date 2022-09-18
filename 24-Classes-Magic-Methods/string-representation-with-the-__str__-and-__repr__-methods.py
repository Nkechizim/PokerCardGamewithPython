class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f'Card("{self.rank}", "{self.suit}")'

c = Card("Ace", "Spades")
print(c)
print(repr(c))

d = Card("King", "Hearts")
print(d)
print(repr(d))

#technically the __str__ is the default but if it is not provided then the __repr__ is used
#the __str__ should be a more user friendly documentation of the object 
#while the __repr__ is more technical representation, they're both called behind the scenes