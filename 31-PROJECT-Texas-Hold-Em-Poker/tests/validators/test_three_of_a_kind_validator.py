import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.cards = [
            Card("5", "Hearts"),
            Card("7", "Clubs"),
            Card("Queen", "Diamonds"),
            Card("Queen", "Hearts"),
            Card("Queen", "Spades")
        ]

    def test_cards_have_three_of_a_kind(self):
        validator = ThreeOfAKindValidator(self.cards)
        self.assertEqual(validator.is_valid(), "Three of a Kind")

    def test_returns_three_of_a_kind_from_cards(self):
        validator = ThreeOfAKindValidator(self.cards)
        self.assertEqual(
            validator.valid_cards(), [
                Card("Queen", "Diamonds"), Card("Queen", "Hearts"), 
                Card("Queen", "Spades")]
        )