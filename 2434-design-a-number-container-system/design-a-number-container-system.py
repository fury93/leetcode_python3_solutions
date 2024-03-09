from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.indexNum = dict()
        self.numIndexes = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.indexNum:
            oldNum = self.indexNum[index]
            self.numIndexes[oldNum].remove(index)
        self.indexNum[index] = number
        self.numIndexes[number].add(index)

    def find(self, number: int) -> int:
        return self.numIndexes[number][0] if self.numIndexes[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)