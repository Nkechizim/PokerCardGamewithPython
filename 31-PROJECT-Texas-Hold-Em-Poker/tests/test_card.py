import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank = "9", suit = "Spades")
        self.assertEqual(card.suit, "Spades")

    def test_card_knows_its_rank_index(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank_index, 10)

    def test_has_string_representation_with_rank_suit(self):
        card = Card("Jack", "Clubs")
        self.assertEqual(str(card), "Jack of Clubs")

    def test_has_tech_representation_with_rank_suit(self):
        card = Card(rank = "9", suit = "Spades")
        self.assertEqual(repr(card), "Card('9', 'Spades')")

    def test_card_has_four_possible_suits(self):
        self.assertEqual(
            Card.SUITS, 
            ("Hearts", "Spades", "Clubs", "Diamonds")
        )

    def test_card_has_thirtheen_possible_ranks(self):
        self.assertEqual(
            Card.RANKS, 
            ("2", "3", "4", "5", "6", "7", "8", "9", "10", 
                "Jack", "Queen", "King", "Ace"))

    def test_card_only_allows_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Diamonds")
            Card(rank = 2, suit = "Diamonds")

    def test_card_only_allows_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank = "2", suit = "Diamond")
            Card(rank = "2", suit = "Dismonds")

    def test_can_create_52_cards(self):
        cards = Card.create_52_cards()
        self.assertEqual(len(cards), 52)
        self.assertIsInstance(cards[0], Card)
        self.assertIsInstance(cards[-1], Card)

    def test_equality_between_two_card_instances(self):
        card = Card(rank = "6", suit = "Diamonds")
        card1 = Card("6", "Diamonds")
        self.assertEqual(card, card1)
    
    def test_cards_are_being_sorted(self):
        card = Card(rank = "6", suit = "Diamonds")
        card1 = Card("5", "Hearts")
        evaluation = card1 < card
        self.assertEqual(evaluation, True)

    def test_sorts_cards(self):
        card = Card(rank = "6", suit = "Diamonds")
        card1 = Card("5", "Hearts")
        card2 = Card("5", "Clubs")
        card3 = Card("Ace", "Spades")
        card4 = Card("Queen", "Hearts")
        unsorted_cards = [card, card1, card2, card3, card4]
        # sorted_cards = Card.sort_cards(unsorted_cards)

        # self.assertEqual(
        #     sorted_cards, [card1, card2, card, card4, card3]
        # )

        unsorted_cards.sort()

        self.assertEqual(
            unsorted_cards,
            [card2, card1, card, card4, card3]
        )