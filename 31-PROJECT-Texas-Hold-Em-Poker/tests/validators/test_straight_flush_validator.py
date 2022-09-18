import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.cards = [
            Card("7", "Clubs"),
            Card("8", "Spades"),
            Card("9", "Clubs"), 
            Card("10", "Clubs"),
            Card("Jack", "Clubs"),
            Card("Queen", "Clubs"),
            Card("King", "Clubs")
        ]

    def test_cards_dont_have_5_consecutive_cards_with_the_same_suit(self):       
        cards = [
            Card("8", "Spades"), Card("9", "Clubs"), 
            Card("10", "Clubs"), Card("Jack", "Clubs"),
            Card("Queen", "Hearts"), Card("King", "Clubs")
        ]
        validator = StraightFlushValidator(cards)
        self.assertEqual(validator.is_valid(), None)

    def test_cards_have_5_consecutive_cards_with_the_same_suit(self):       
        validator = StraightFlushValidator(self.cards)
        self.assertEqual(validator.is_valid(), "Straight Flush")

    def test_returns_5_consecutive_cards_with_the_same_suit(self):
        validator = StraightFlushValidator(self.cards)
        self.assertEqual(
            validator.valid_cards(), [
            Card("9", "Clubs"),
            Card("10", "Clubs"),
            Card("Jack", "Clubs"),
            Card("Queen", "Clubs"),
            Card("King", "Clubs")]
        )