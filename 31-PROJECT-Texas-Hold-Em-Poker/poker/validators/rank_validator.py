class RankValidator():
    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts

    def _rank_counts(self, count):
        rank_counts = []
        for rank_count in self._card_rank_counts.values():
            rank_counts.append(rank_count)
        return rank_counts.count(count)