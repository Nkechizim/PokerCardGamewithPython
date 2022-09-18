import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.cards = [
            Card("5", "Hearts"),
            Card("7", "Clubs"),
            Card("7", "Hearts"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Spades")
        ]

    def test_validates_cards_have_exactly_two_pair(self):
        validator = TwoPairValidator(self.cards)
        self.assertEqual(validator.is_valid(), "Two Pair")
    
    def test_returns_two_pair_from_cards(self):
        validator = TwoPairValidator(self.cards)
        self.assertEqual(
            validator.valid_cards(), [
                Card("7", "Clubs"), Card("7", "Hearts"),
                Card("Ace", "Diamonds"), Card("Ace", "Spades")]
        )