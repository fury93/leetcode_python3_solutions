from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.timeToPrice = defaultdict(int)
        self.prices = SortedList()
        self.maxTime = 0

    def update(self, timestamp: int, price: int) -> None:
        self.prices.discard(self.timeToPrice[timestamp])
        self.prices.add(price)
        self.timeToPrice[timestamp] = price
        self.maxTime = max(self.maxTime, timestamp)

    def current(self) -> int:
        return self.timeToPrice[self.maxTime]

    def maximum(self) -> int:
        if not self.prices: return 0
        return self.prices[-1]

    def minimum(self) -> int:
        if not self.prices: return 0
        return self.prices[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()