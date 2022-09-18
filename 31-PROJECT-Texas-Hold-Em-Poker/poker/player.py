# from card import Card
# from deck import Deck
# from hand import Hand

class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def add_cards_to_hand(self, cards):
        self.hand.add_cards(cards)

    def best_hand(self):
        return self.hand.best_rank()
    
    def wants_to_fold(self):
        return False

    def __gt__(self, other):
        current_player_best_rank_index = self.best_hand()[0]
        other_player_best_rank_index = other.best_hand()[0]
        return current_player_best_rank_index < other_player_best_rank_index