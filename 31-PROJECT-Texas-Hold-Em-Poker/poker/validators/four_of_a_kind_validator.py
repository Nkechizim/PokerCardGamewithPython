from poker.validators import RankValidator

class FourOfAKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards

    def is_valid(self):
        if self._rank_counts(4) == 1:
            return "Four of a kind"

    def valid_cards(self):
        return [
            card
            for rank, values in self._card_rank_counts.items()
            for card in self.cards
            if values == 4 and rank == card.rank
        ]