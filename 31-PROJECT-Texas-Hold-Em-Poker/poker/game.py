class Game():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def play(self):
        self._shuffle_deck()
        self._deal_initial_two_cards_to_players()
        self._removes_player_if_wants_to_fold()
        
        self._deal_flop_cards_to_players()
        self._removes_player_if_wants_to_fold()

        self._deal_turn_card_to_players()
        self._removes_player_if_wants_to_fold()

        self._deal_river_card_to_players()
        self._removes_player_if_wants_to_fold()

    def _shuffle_deck(self):
        self.deck.shuffle()

    def _deal_initial_two_cards_to_players(self):
        for player in self.players:
            cards = self.deck.remove_cards(2)
            player.add_cards_to_hand(cards)

    def _deal_community_cards_to_players(self, number):
        cards = self.deck.remove_cards(number)
        for player in self.players:
            player.add_cards_to_hand(cards)

    def _deal_flop_cards_to_players(self):
        self._deal_community_cards_to_players(3)

    def _deal_turn_card_to_players(self):
        self._deal_community_cards_to_players(1)

    def _deal_river_card_to_players(self):
        self._deal_community_cards_to_players(1)

    def _removes_player_if_wants_to_fold(self):
        for player in self.players:
            if player.wants_to_fold():
                self.players.remove(player)