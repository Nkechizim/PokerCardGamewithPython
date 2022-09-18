import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.cards = [
            Card("8", "Diamonds"), 
            Card("9", "Clubs"), 
            Card("10", "Clubs"),
            Card("Jack", "Clubs"),
            Card("Queen", "Clubs"),
            Card("King", "Clubs"),
            Card("Ace", "Clubs")
        ]

    def test_cards_dont_have_5_royal_flush(self):       
        cards = [
            Card("9", "Clubs"), Card("10", "Clubs"), 
            Card("Jack", "Clubs"), Card("Queen", "Clubs"), 
            Card("King", "Clubs"), Card("Ace", "Spades"), 
        ]
        validator = RoyalFlushValidator(cards)
        self.assertEqual(validator.is_valid(), None)

    def test_cards_have_straight_flush_ending_with_ace(self):
        validator = RoyalFlushValidator(self.cards)
        self.assertEqual(validator.is_valid(), "Royal Flush")

    def test_returns_5_cards_constituting_royal_flush(self):
        validator = RoyalFlushValidator(self.cards)
        self.assertEqual(
            validator.valid_cards(), [
            Card("10", "Clubs"),
            Card("Jack", "Clubs"),
            Card("Queen", "Clubs"),
            Card("King", "Clubs"),
            Card("Ace", "Clubs"),]
        )