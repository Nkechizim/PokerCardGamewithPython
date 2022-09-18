from poker.validators import StraightFlushValidator as straight_flush

class RoyalFlushValidator():
    def __init__(self, cards):
        self.cards = cards

    def is_valid(self):
        if straight_flush(self.cards).is_valid() != None:
            royal_card = straight_flush(self.cards).valid_cards()
            if royal_card[-1].rank == "Ace":
                return "Royal Flush"

    def valid_cards(self):
        return straight_flush(self.cards).valid_cards()