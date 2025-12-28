class Solution:
    # SPFA
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, w in times:
            adjList[u].append((v, w))

        bestTime = [0] + [math.inf] * n
        bestTime[k] = 0

        q = deque([k])
        inQueue = [False] * (n + 1)
        inQueue[k] = True

        while q:
            u = q.popleft()
            inQueue[u] = False

            for v, w in adjList[u]:
                newTime = bestTime[u] + w
                
                if newTime < bestTime[v]:
                    bestTime[v] = newTime
                    if not inQueue[v]:
                        q.append(v)
                        inQueue[v] = True
               

        res = max(bestTime)
        return -1 if res == math.inf else res