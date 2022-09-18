import unittest
from poker.hand import Hand
from poker.card import Card
from poker.validators import PairValidator

class HandTest(unittest.TestCase):
    def test_hand_has_tech_representation(self):
        cards = [Card("Queen", "Spades"), Card("Jack", "Clubs")]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(repr(hand), 
            "['Jack of Clubs', 'Queen of Spades']")

    def test_hand_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_receives_stores_card_and_sorts(self):
        hand = Hand()
        cards = [Card("Queen", "Spades"), Card("Jack", "Clubs")]
        hand.add_cards(cards)
        self.assertEqual(hand.cards, [Card("Jack", "Clubs"), Card("Queen", "Spades")])

    def test_interacts_with_validators(self):
        class HandWithOneValidator(Hand):
            VALIDATORS = (PairValidator,)

        cards = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Hearts")
        ]

        hand = HandWithOneValidator()
        hand.add_cards(cards)
        self.assertEqual(
            hand.best_rank(), 
            (0, "Pair", [Card("Ace", "Diamonds"), Card("Ace", "Hearts")]))