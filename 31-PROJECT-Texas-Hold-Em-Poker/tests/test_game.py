import unittest
from unittest.mock import MagicMock, call

from poker.game import Game
from poker.card import Card

class GameTest(unittest.TestCase):
    def setUp(self):
        self.first_two_cards = [Card("9", "Hearts"), Card("Jack", "Diamonds")]
        self.next_two_cards = [Card("8", "Hearts"), Card("Ace", "Diamonds")]
        self.community_cards_flop = [
            Card("9", "Spades"), 
            Card("8", "Clubs"), 
            Card("10", "Spades")]
        self.community_cards_turn = [Card("2", "Spades")]
        self.community_cards_river = [Card("4", "Clubs")]

    def test_stores_deck_and_players(self):
        mock_deck = MagicMock()
        mock_players = [MagicMock(), MagicMock()]
        game =  Game(deck = mock_deck, players = mock_players)

        self.assertEqual(game.deck, mock_deck)
        self.assertEqual(game.players, mock_players)

    def test_game_play_shuffles_deck(self):
        mock_deck = MagicMock()
        mock_players = [MagicMock(), MagicMock()]
        game =  Game(deck = mock_deck, players = mock_players)

        game.play()
        mock_deck.shuffle.assert_called_once()

    def test_deals_two_initial_cards_to_each_player_from_deck(self):
        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards, 
            self.next_two_cards,
            self.community_cards_flop,
            self.community_cards_turn,
            self.community_cards_river
        ]

        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        mock_players = [mock_player1, mock_player2]
        game =  Game(deck = mock_deck, players = mock_players)

        game.play()
        mock_deck.remove_cards.assert_has_calls([call(2), call(2)])

        mock_player1.add_cards_to_hand.assert_has_calls([call(self.first_two_cards)])
        mock_player2.add_cards_to_hand.assert_has_calls([call(self.next_two_cards)])

    def test_removes_player_if_wants_to_fold(self):
        deck = MagicMock()
        player1 = MagicMock()
        player2 = MagicMock()
        player1.wants_to_fold.return_value = True
        player2.wants_to_fold.return_value = False
        players = [player1, player2]

        game = Game(deck, players)
        game.play()
        self.assertEqual(game.players, [player2])

    def test_deals_the_same_community_cards_to_all_players(self):
        deck = MagicMock()

        player1 = MagicMock()
        player1.wants_to_fold.return_value = False
        player2 = MagicMock()
        player2.wants_to_fold.return_value = False
        players = [player1, player2]
        
        deck.remove_cards.side_effect = [
            self.first_two_cards, 
            self.next_two_cards, 
            self.community_cards_flop,
            self.community_cards_turn,
            self.community_cards_river
        ]

        game = Game(deck, players)

        game.play()

        deck.remove_cards.assert_has_calls([call(3), call(1), call(1)])

        calls = [
            call(self.community_cards_flop),
            call(self.community_cards_turn),
            call(self.community_cards_river)
        ]

        player1.add_cards_to_hand.assert_has_calls(calls)
        player2.add_cards_to_hand.assert_has_calls(calls)