#from sortedcontainers import SortedList
class LogSystem2:

    def __init__(self):
        self.logs = SortedList()
        self.mask = {"Year": 4, "Month": 7, "Day": 10, "Hour":13, "Minute":16, "Second":19}

    def put(self, id: int, timestamp: str) -> None:
        self.logs.add((timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        sliceIdx = self.mask[granularity]
        start = start[:sliceIdx]
        end = end[:sliceIdx]
        startIdx = bisect_left(self.logs, start, key = lambda x: x[0][:sliceIdx])
        endIdx = bisect_right(self.logs, end, key = lambda x: x[0][:sliceIdx])

        return set(self.logs[i][1] for i in range(startIdx, endIdx))

class LogSystem:

    def __init__(self):
        self.logs = {}

    def put(self, id, timestamp):
        if timestamp not in self.logs:
            self.logs[timestamp] = set()
        self.logs[timestamp].add(id)

    def retrieve(self, start, end, granularity):
        index = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second': 19}[granularity]
        start, end = start[:index], end[:index]

        # Collecting and sorting unique IDs from logs in the specified range
        ids = set()
        for timestamp in self.logs:
            if start <= timestamp[:index] <= end:
                ids.update(self.logs[timestamp])

        return sorted(ids)

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)