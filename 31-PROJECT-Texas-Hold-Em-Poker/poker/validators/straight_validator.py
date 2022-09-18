class StraightValidator():
    def __init__(self, cards):
        self.cards = cards

    def _seperates_cards_into_batches_of_five(self):
        batch_1 = self.cards[:5]
        batch_2 = self.cards[1:6]
        batch_3 = self.cards[2:7]

        return [batch_1, batch_2, batch_3]

    def _converts_batch_of_cards_to_their_rank_index(self):
        rank_indexes = []
        batches = self._seperates_cards_into_batches_of_five()
        for position, batch in enumerate(batches):
            rank_indexes.append([])
            for card in batch:
                rank_indexes[position].append(card.rank_index)

        return rank_indexes

    @property
    def _collection_of_5_consecutive_cards(self):
        straight_cards = []
        batches = self._seperates_cards_into_batches_of_five()
        rank_indexes = self._converts_batch_of_cards_to_their_rank_index()

        #alternate syntax
        for index_position, rank_index in enumerate(rank_indexes):
            if len(rank_index) == 5:
                if rank_index == list(range(rank_index[0], rank_index[-1] + 1)):
                    straight_cards.append(batches[index_position])

        return straight_cards

    def is_valid(self):
        if len(self._collection_of_5_consecutive_cards) >= 1:
            return "Straight"
        

    def valid_cards(self):
        return self._collection_of_5_consecutive_cards[-1]