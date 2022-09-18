import random

class Player():
    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories

    @property
    def win_ratio(self):
        return self.victories / self.games_played

class HumanPlayer(Player):
    def make_move(self): 
        print("Let player make move!")

class ComputerPlayer(Player):
    def make_move(self): 
        print("Run advanced algorithm to calculate best move!")

hp = HumanPlayer(games_played = 30, victories = 15)
cp = ComputerPlayer(1000, victories = 999)

print(hp.win_ratio)
print(cp.win_ratio)

game_players = [hp, cp]
starting_player = random.choice(game_players)
starting_player.make_move()

print()

class DentalHealthItem():
    def __init__(self):
        self.price = 100
        
class Toothbrush(DentalHealthItem):
    def use(self):
        return "Brushing the teeth"
        
class Floss(DentalHealthItem):
    def use(self):
        return "Flossing the teeth"
        
class Mouthwash(DentalHealthItem):
    def use(self):
        return "Washing the teeth"
        
toothbrush = Toothbrush()
floss = Floss()
mouthwash = Mouthwash()
dental_health_kit = [toothbrush, floss, mouthwash]
random.shuffle(dental_health_kit)
#print(dental_health_kit)


for action in dental_health_kit:
    print(action.use())