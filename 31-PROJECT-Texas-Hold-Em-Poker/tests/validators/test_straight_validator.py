import unittest

from poker.card import Card
from poker.validators import StraightValidator

class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        self.cards = [
            Card("2", "Spades"),
            Card("4", "Diamonds"),
            Card("5", "Hearts"),
            Card("6", "Clubs"),
            Card("7", "Spades"), 
            Card("8", "Hearts"),
            Card("9", "Diamonds")
        ]

    def test_validates_cards_have_consecutive_five_cards(self):
        validator = StraightValidator(self.cards)
        self.assertEqual(validator.is_valid(), "Straight")

    def test_returns_consecutive_five_cards(self):
        validator = StraightValidator(self.cards)
        self.assertEqual(
            validator.valid_cards(), [
            Card("5", "Hearts"),
            Card("6", "Clubs"),
            Card("7", "Spades"), 
            Card("8", "Hearts"),
            Card("9", "Diamonds")]
        )