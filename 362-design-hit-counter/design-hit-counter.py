class HitCounter:

    def __init__(self, maxTime = 300):
        self.cnt = 0
        self.maxTime = maxTime
        self.hits = deque(maxlen = maxTime) # ([timestamp, count])
        
    def hit(self, timestamp: int) -> None:
        if not self.hits or self.hits[-1][0] < timestamp:
            self.hits.append([timestamp, 1])
        else:
            self.hits[-1][1] += 1
        self.cnt += 1 

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][0] <= timestamp - self.maxTime:
            self.cnt -= self.hits.popleft()[1]
        return self.cnt

class HitCounter2:

    def __init__(self, maxTime = 300):
        self.lastHitIdx = 0
        self.maxTime = maxTime
        self.hits = [[0, 0]] * self.maxTime
        
    def hit(self, timestamp: int) -> None:
        idx = timestamp % self.maxTime
        if self.hits[idx][0] < timestamp:
            self.hits[idx] = [timestamp, 1]
        else:
            self.hits[idx][1] += 1
        self.lastHitIdx = idx

    def getHits(self, timestamp: int) -> int:
        if timestamp - self.maxTime > self.hits[self.lastHitIdx][0]: return 0
        return sum(cnt for t, cnt in self.hits if timestamp - t < self.maxTime)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)