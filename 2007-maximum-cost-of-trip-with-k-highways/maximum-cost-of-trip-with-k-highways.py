class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        if k + 1 > n:
            return -1
        
        graph = defaultdict(list)
        for city_a, city_b, cost in highways:
            graph[city_a].append((city_b, cost))
            graph[city_b].append((city_a, cost))
        
        @cache
        def dp(city, bitmask):
            cities_visited = bitmask.bit_count()
            if cities_visited == k + 1:
                return 0
            
            answer = -1
            for nei_city, highway_cost in graph[city]:
                if not (bitmask >> nei_city) & 1:
                    nei_answer = dp(nei_city, bitmask | (1 << nei_city))
                    if nei_answer != -1:
                        answer = max(answer, highway_cost + nei_answer)
            return answer
        
        return max(dp(city, 1 << city) for city in range(n))