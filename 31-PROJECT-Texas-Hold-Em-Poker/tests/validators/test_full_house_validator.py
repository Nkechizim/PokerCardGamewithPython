import unittest

from poker.card import Card
from poker.validators import FullHouseValidator

class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.cards = [
            Card("3", "Clubs"),
            Card("3", "Diamonds"),
            Card("3", "Hearts"), 
            Card("8", "Clubs"),
            Card("8", "Spades"),
            Card("Queen", "Diamonds")
        ]

    def test_validates_cards_have_three_of_a_kind_and_a_pair(self):    
        validator = FullHouseValidator(self.cards)
        self.assertEqual(validator.is_valid(), "Full House")

    def test_returns_cards_with_three_of_a_kind_and_pair(self):
        validator = FullHouseValidator(self.cards)
        self.assertEqual(
            validator.valid_cards(), [
            Card("3", "Clubs"),
            Card("3", "Diamonds"),
            Card("3", "Hearts"), 
            Card("8", "Clubs"),
            Card("8", "Spades")]
        )