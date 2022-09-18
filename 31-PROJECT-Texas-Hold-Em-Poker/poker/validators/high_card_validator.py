class HighCardValidator():
    def __init__(self, cards):
        self.cards = cards

    def is_valid(self):
        if len(self.cards) >= 2:
            return "High Card"

    def valid_cards(self):
        return self.cards[-1:]