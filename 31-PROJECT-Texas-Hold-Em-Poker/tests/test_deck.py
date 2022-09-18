import unittest
from unittest.mock import patch

from poker.deck import Deck
from poker.card import Card

class DeckTest(unittest.TestCase):
    def test_stores_no_card_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards, []
        )
    
    def test_add_cards_to_deck(self):
        card = Card("Queen", "Hearts")
        card1 = Card("King", "Spades")
        deck = Deck()
        deck.add_cards([card, card1])
        self.assertEqual(deck.cards, [card, card1])

    def test_to_check_the_length_of_a_deck(self):
        card = Card("Queen", "Hearts")
        card1 = Card("King", "Spades")
        deck = Deck()
        deck.add_cards([card, card1])
        self.assertEqual(len(deck), 2)

    @patch('random.shuffle')
    def test_deck_shuffles_cards(self, mock_shuffle):
        deck = Deck()
        cards = [
            Card("Queen", "Diamonds"),
            Card("5", "Hearts"),
            Card("7", "Clubs"),
            Card("Queen", "Hearts")
        ]
        deck.add_cards(cards)
        deck.shuffle()

        mock_shuffle.assert_called_once_with(cards)

    def test_removes_cards_from_deck(self):
        deck = Deck()
        cards = [
            Card("Queen", "Diamonds"),
            Card("5", "Hearts"),
            Card("7", "Clubs"),
            Card("Queen", "Hearts")
        ]
        deck.add_cards(cards)

        self.assertEqual(deck.remove_cards(2), [Card("Queen", "Diamonds"),
            Card("5", "Hearts")])
        self.assertEqual(deck.cards, [Card("7", "Clubs"), Card("Queen", "Hearts")])
