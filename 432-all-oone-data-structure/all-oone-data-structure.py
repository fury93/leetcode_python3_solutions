from sortedcontainers import SortedList
class AllOne:

    def __init__(self):
        self.data = defaultdict(int) #SortedDict()
        self.count = SortedList()

    def inc(self, key: str) -> None:
        self.data[key] += 1
        cnt = self.data[key]
        if cnt > 1:
            self.count.discard((cnt-1, key))
        self.count.add((cnt, key))

    def dec(self, key: str) -> None:
        self.data[key] -= 1
        cnt = self.data[key]
        self.count.discard((cnt + 1, key))
        
        if cnt > 0:
            self.count.add((cnt, key))
        else:
            self.data.pop(key)
        

    def getMaxKey(self) -> str:
        if not self.count: return ''
        return self.count[-1][1]
        

    def getMinKey(self) -> str:
        if not self.count: return ''
        return self.count[0][1]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()