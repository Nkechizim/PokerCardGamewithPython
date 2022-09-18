import unittest

from poker.card import Card
from poker.validators import FlushValidator

class FlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.cards = [
            Card("3", "Diamonds"),
            Card("6", "Diamonds"),
            Card("7", "Diamonds"), 
            Card("8", "Diamonds"),
            Card("9", "Clubs"),
            Card("Queen", "Diamonds"),
            Card("Ace", "Diamonds")
        ]

    def test_validates_5_cards_have_the_same_suit(self): 
        validator = FlushValidator(self.cards)
        self.assertEqual(validator.is_valid(), "Flush")

    def test_returns_five_cards_with_the_same_suit(self):
        validator = FlushValidator(self.cards)
        self.assertEqual(
            validator.valid_cards(), [
            Card("6", "Diamonds"),
            Card("7", "Diamonds"), 
            Card("8", "Diamonds"),
            Card("Queen", "Diamonds"),
            Card("Ace", "Diamonds")]
        )