from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.data = SortedList()
        self.idx = 0

    def add(self, name: str, score: int) -> None:
        self.data.add((-score, name))

    def get(self) -> str:
        res = self.data[self.idx][1]
        self.idx += 1
        return res


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()