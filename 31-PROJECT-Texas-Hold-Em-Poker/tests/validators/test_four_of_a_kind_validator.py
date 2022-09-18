import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.cards = [
            Card("3", "Clubs"),
            Card("4", "Diamonds"),
            Card("8", "Hearts"), 
            Card("8", "Clubs"),
            Card("8", "Spades"),
            Card("8", "Diamonds"),
            Card("Queen", "Diamonds")
        ]

    def test_validates_cards_have_four_of_the_same_rank(self):
        validator = FourOfAKindValidator(self.cards)
        self.assertEqual(validator.is_valid(), "Four of a kind")

    def test_returns_the_four_cards_with_same_rank(self):
        validator = FourOfAKindValidator(self.cards)
        self.assertEqual(
            validator.valid_cards(), [
            Card("8", "Hearts"), 
            Card("8", "Clubs"),
            Card("8", "Spades"),
            Card("8", "Diamonds")]
        )
