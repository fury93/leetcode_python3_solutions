from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.data = SortedList()
        self.idx = -1

    def add(self, name: str, score: int) -> None:
        self.data.add((-score, name))

    def get(self) -> str:
        self.idx += 1
        return self.data[self.idx][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()