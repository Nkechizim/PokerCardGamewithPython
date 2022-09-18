class FilmMaker():
    def give_interview(self):
        print("I love making movies!")

class Director(FilmMaker):
    pass

class ScreenWriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts")

class JackOfAllTrades(Director, ScreenWriter):
    pass

jack_of_all_trade = JackOfAllTrades()
jack_of_all_trade.give_interview()

print(JackOfAllTrades.mro())