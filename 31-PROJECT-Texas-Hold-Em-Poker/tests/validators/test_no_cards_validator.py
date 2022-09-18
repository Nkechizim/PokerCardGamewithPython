import unittest

from poker.card import Card
from poker.validators import NoCardsValidator

class NoCardsValidatorTest(unittest.TestCase):
    def test_validates_hand_has_no_cards(self):
        cards = []
        validator = NoCardsValidator(cards)
        self.assertEqual(validator.is_valid(), "No Card")

    def test_returns_no_card_from_cards(self):
        cards = []
        validator = NoCardsValidator(cards)
        self.assertEqual(validator.valid_cards(), [])