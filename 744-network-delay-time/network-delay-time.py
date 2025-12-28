class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = deque([(k, 0)])
        signalTime = [0] + [math.inf] * n
        adjList = defaultdict(list)
        for u, v, w in times:
            adjList[u].append((v, w))

        while q:
            u, time = q.popleft()
            
            if signalTime[u] > time:
                signalTime[u] = time
                for v, w in adjList[u]:
                    q.append((v, time + w))

        maxTime = max(signalTime)
        return -1 if maxTime == math.inf else maxTime