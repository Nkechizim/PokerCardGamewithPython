from poker.validators import (StraightValidator as straight,
FlushValidator as flush)

class StraightFlushValidator(straight):
    def __init__(self, cards):
        self.cards = cards

    @property
    def _collection_of_5_consecutive_cards_with_the_same_suit(self):
        straight_flush = []
        if straight(self.cards).is_valid() != None:
            for straight_pack in self._collection_of_5_consecutive_cards:
                if flush(straight_pack).is_valid() != None:
                    straight_flush.append(straight_pack)
        
        return straight_flush

    def is_valid(self):
       if len(self._collection_of_5_consecutive_cards_with_the_same_suit) >= 1:
            return "Straight Flush"

    def valid_cards(self):
        return self._collection_of_5_consecutive_cards_with_the_same_suit[-1]