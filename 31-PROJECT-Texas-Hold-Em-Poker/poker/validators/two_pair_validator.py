from poker.validators import RankValidator

class TwoPairValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards

    def is_valid(self):
        if self._rank_counts(2) == 2:
            return "Two Pair"

    def valid_cards(self):
        return [
            card
            for rank, values in self._card_rank_counts.items()
            for card in self.cards
            if values == 2 and rank == card.rank
        ]