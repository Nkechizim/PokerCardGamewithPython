import unittest

from poker.card import Card
from poker.validators import HighCardValidator

class HighCardValidatorTest(unittest.TestCase):
    def test_validates_high_card_is_best_rank(self):
        cards = [
            Card("2", "Hearts"),
            Card("3", "Hearts")
        ]
        validator = HighCardValidator(cards)
        self.assertEqual(validator.is_valid(), "High Card")

    def test_returns_high_card_from_card_collection(self):
        ace_of_diamonds = Card("Ace", "Diamonds")

        cards = [
            Card("7", "Hearts"),
            Card("9", "Spades"),
            Card("10", "Clubs"),
            Card("Jack", "Hearts"),
            ace_of_diamonds
        ]
        validator = HighCardValidator(cards)

        self.assertEqual(validator.valid_cards(), [ace_of_diamonds])