class FlushValidator():
    def __init__(self, cards):
        self.cards = cards

    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts

    def is_valid(self):
        for suit_count in self._card_suit_counts.values():
            if suit_count >= 5:
                return "Flush"

    def valid_cards(self):
        cards = [
            card
            for suit, values in self._card_suit_counts.items()
            for card in self.cards
            if values >= 5 and suit == card.suit
        ]
        return cards[-5:]