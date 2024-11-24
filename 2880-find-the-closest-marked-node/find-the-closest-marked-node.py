class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        
        ## use dijkstra and return the minimum
        ## using dijkstra find minimum distance of all nodes from s
        ## then find the min of distances for nodes that belong to marked array
        graph = {x:[] for x in range(n)}

        for v1, v2, wt in edges:
            graph[v1].append([v2,wt])

        ## dijkstra algorithm
        visited = set()
        pq = []
        dist = {x:float('inf') for x in range(n)}
        dist[s] = 0
        heapq.heappush(pq, (0, s))

        while pq:
            cost, node = heapq.heappop(pq)
            visited.add(node)

            for nei, nei_cost in graph[node]:
                if nei in visited:
                    continue
                new_cost = cost + nei_cost
                if dist[nei] > new_cost:
                    dist[nei] = new_cost
                    heapq.heappush(pq, (new_cost, nei))

        ## iterate over the marked list to find min dist of any node from s
        ans = float('inf')
        for node in marked:
            ans = min(ans, dist[node])

        return ans if ans!=float('inf') else -1

        