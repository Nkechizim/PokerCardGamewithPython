class NoCardsValidator():
    def __init__(self, cards):
        self.cards = cards

    def is_valid(self):
        if len(self.cards) == 0:
            return "No Card"

    def valid_cards(self):
        return self.cards