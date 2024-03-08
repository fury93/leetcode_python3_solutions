class Leaderboard:

    def __init__(self):
        self.playersScore = Counter()

    def addScore(self, playerId: int, score: int) -> None:
        self.playersScore[playerId] += score

    def top(self, K: int) -> int:
        return sum(score for _, score in self.playersScore.most_common(K))

    def reset(self, playerId: int) -> None:
        self.playersScore[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)