class Card():
    SUITS = ("Hearts", "Spades", "Clubs", "Diamonds")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", 
                "Jack", "Queen", "King", "Ace")

    @classmethod
    def create_52_cards(cls):
        return [cls(rank, suit) for suit in cls.SUITS for rank in cls.RANKS]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid Rank. Rank must be one of these {self.RANKS}")

        if suit not in self.SUITS:
            raise ValueError(f"Invalid Suit. Suit must be one of these {self.SUITS}")
        
        self.rank = rank
        self.suit = suit
        self.rank_index = self.RANKS.index(rank)

    # @classmethod
    # def sort_cards(cls, unsorted_cards):
    #     card_index = [card.rank_index for card in unsorted_cards]
    #     card_index.sort()
    #     sorted_cards = []
    #     for index in card_index:
    #         for card in unsorted_cards:
    #             if index == card.rank_index and card not in sorted_cards:
    #                 sorted_cards.append(card)

    #     return sorted_cards

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit < other.suit
        return self.rank_index < other.rank_index

