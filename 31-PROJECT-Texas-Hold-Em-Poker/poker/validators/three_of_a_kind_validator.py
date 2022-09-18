from poker.validators import RankValidator

class ThreeOfAKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards

    def is_valid(self):
        if self._rank_counts(3) == 1:
            return "Three of a Kind"

    def valid_cards(self):
        return [
            card
            for rank, values in self._card_rank_counts.items()
            for card in self.cards
            if values == 3 and rank == card.rank
        ]