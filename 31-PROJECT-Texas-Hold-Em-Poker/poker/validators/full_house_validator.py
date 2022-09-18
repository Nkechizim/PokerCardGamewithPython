from poker.validators import (
    ThreeOfAKindValidator as three_of_a_kind, 
    PairValidator as pair)

class FullHouseValidator():
    def __init__(self, cards):
        self.cards = cards

    def is_valid(self):
        if three_of_a_kind(self.cards).is_valid() != None and pair(self.cards).is_valid() != None:
            return "Full House"

    def valid_cards(self):
        cards = []
        cards.extend(three_of_a_kind(self.cards).valid_cards())
        cards.extend(pair(self.cards).valid_cards())
        cards.sort()
        return cards