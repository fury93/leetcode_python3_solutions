class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.outer = 0
        self.inner = 0

    def __moveToNext(self):
        while self.outer < len(self.vec) and len(self.vec[self.outer]) == self.inner:
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        val = self.vec[self.outer][self.inner]
        self.inner += 1
        return val
        
    def hasNext(self) -> bool:
        self.__moveToNext()
        return self.outer < len(self.vec)