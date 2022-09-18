from poker.validators import (
    NoCardsValidator as no_card, HighCardValidator as high_card,
    PairValidator as pair, TwoPairValidator as two_pair,
    ThreeOfAKindValidator as three_of_a_kind, StraightValidator as straight,
    FlushValidator as flush, FullHouseValidator as full_house,
    FourOfAKindValidator as four_of_a_kind, StraightFlushValidator as straight_flush,
    RoyalFlushValidator as royal_flush)

class Hand():
    VALIDATORS = (
        royal_flush, straight_flush, four_of_a_kind,
        full_house, flush, straight, three_of_a_kind,
        two_pair, pair, high_card, no_card
    )

    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    def __repr__(self):
        tech_rep = str([str(card) for card in self.cards]) 
        return tech_rep

    def best_rank(self):
        for index, validator_klass in enumerate(self.VALIDATORS):
            validator = validator_klass(self.cards)
            if validator.is_valid() != None:
                return (index, validator.is_valid(),validator.valid_cards())