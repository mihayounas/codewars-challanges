class User:
    RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, activity_rank):
        if activity_rank not in self.RANKS:
            raise ValueError("Invalid activity rank")

        rank_diff = self.RANKS.index(activity_rank) - self.RANKS.index(self.rank)
        
        if rank_diff == 0:
            self.progress += 3
        elif rank_diff == -1:
            self.progress += 1
        elif rank_diff > 0:
            self.progress += 10 * rank_diff * rank_diff

        if self.progress >= 100:
            rank_steps = self.progress // 100
            self.rank = self.RANKS[min(self.RANKS.index(self.rank) + rank_steps, len(self.RANKS) - 1)]
            self.progress %= 100

        if self.rank == 8:
            self.progress = 0

