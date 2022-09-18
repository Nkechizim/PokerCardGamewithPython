from poker.card import Card
from poker.deck import Deck
from poker.game import Game
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()
hand3 = Hand()
hand4 = Hand()

player1 = Player(name="Nk", hand = hand1)
player2 = Player(name="Awy", hand= hand2)
player3 = Player(name="Didi", hand= hand3)
player4 = Player(name="Ify", hand= hand4)
players = [player1, player2, player3, player4]

game = Game(deck = deck, players = players)
game.play()

for player in players:
    print(f"{player.name} receives {player.hand}\n")
    index, hand_name, hand_cards = player.best_hand()
    card_string = [str(card) for card in hand_cards]
    hand_cards_string = " and ".join(card_string)
    print(f"{player.name} has a {hand_name} with a {hand_cards_string}\n")

winning_player = max(players)

print(f"The winner is {winning_player.name}.\n")