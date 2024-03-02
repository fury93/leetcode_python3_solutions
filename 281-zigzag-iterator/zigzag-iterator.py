class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.q = deque()
        for i, v in enumerate(self.vectors):
            if v: self.q.append((i, 0))

    def next(self) -> int:
        vector, pos = self.q.popleft()
        val = self.vectors[vector][pos]
        if pos+1 < len(self.vectors[vector]):
            self.q.append((vector, pos+1))
        return val

    def hasNext(self) -> bool:
        return len(self.q) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())