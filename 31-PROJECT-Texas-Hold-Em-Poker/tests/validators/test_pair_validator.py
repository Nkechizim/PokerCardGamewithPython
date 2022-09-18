import unittest

from poker.card import Card
from poker.validators import PairValidator

class PairValidatorTest(unittest.TestCase):
    def test_validates_cards_have_exactly_a_pair(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("Ace", "Hearts")
        ]
        validator = PairValidator(cards)
        self.assertEqual(validator.is_valid(), "Pair")

    def test_returns_pair_from_cards(self):
        cards = [
            Card("7", "Clubs"),
            Card("7", "Hearts"),
            Card("9", "Spades"),
            Card("Jack", "Hearts"),
            Card("Ace", "Diamonds")
        ]

        validator = PairValidator(cards)
        self.assertEqual(
            validator.valid_cards(), [Card("7", "Clubs"), Card("7", "Hearts")]
        )