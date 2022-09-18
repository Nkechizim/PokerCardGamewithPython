import unittest
from unittest.mock import MagicMock

from poker.card import Card
from poker.hand import Hand
from poker.player import Player

class PlayerTest(unittest.TestCase):
    def test_has_name_and_hand(self):
        mock_hand = MagicMock()
        player = Player(name = 'Nk', hand = mock_hand)
        self.assertEqual(player.name, "Nk")
        self.assertEqual(player.hand, mock_hand)

    def test_passes_new_card_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name = 'Nk', hand = mock_hand)
        
        cards = [
            Card("3", "Hearts"),
            Card("2", "Hearts")
        ]
        
        player.add_cards_to_hand(cards)
        mock_hand.add_cards.assert_called_once_with(cards)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player(name = 'Nk', hand = mock_hand)

        self.assertEqual(player.best_hand(), "Straight Flush") 
        mock_hand.best_rank.assert_called()

    def test_decides_to_continue_or_drop_out_of_game(self):
        player = Player(name = 'Nk', hand = Hand())
        self.assertEqual(player.wants_to_fold(), False)

    def test_player_is_sorted_by_best_hand(self):
        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (1, "Straight Flush", [])

        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (4, "Flush", [])

        player1 = Player(name = 'Nk', hand = mock_hand1)
        player2 = Player(name = 'Awy', hand = mock_hand2)

        players = [player1, player2]

        self.assertEqual(
            max(players), player1
        )