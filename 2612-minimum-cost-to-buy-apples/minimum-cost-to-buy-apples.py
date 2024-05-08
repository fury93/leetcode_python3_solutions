class Solution:
    def minCost(
        self, n: int, roads: List[List[int]], appleCost: List[int], k: int
    ) -> List[int]:
        # Store the graph as a list of lists
        # The rows represent the cities (vertices)
        # The columns store an adjacency list of road, cost pairs (edge, weight)
        graph = [[] for _ in range(n)]

        # Add each road to the graph using adjacency lists
        # Store each city at `graph[city - 1]`
        for city_a, city_b, cost in roads:
            graph[city_a - 1].append((city_b - 1, cost))
            graph[city_b - 1].append((city_a - 1, cost))

        # Store the cost to buy an apple in each city 
        # without traveling in the result
        result = list(appleCost)

        # Initialize the min heap (priority queue) with each starting city
        # Each element of the heap is a tuple with the cost and city
        heap = [(apple_cost, start_city) 
                 for start_city, apple_cost in enumerate(appleCost)]

        # Find the minimum cost to buy an apple starting in each city
        while heap:
            # Remove the city with the minimum cost from the top of the heap
            total_cost, curr_city = heapq.heappop(heap)

            # If we have already found a path to buy an apple
            # for cheaper than the local apple cost, skip this city
            if result[curr_city] < total_cost:
                continue

            # Add each neighboring city to the heap if it is cheaper to
            # start there, travel to the current city and buy an apple 
            # than buy in the neighboring city
            for neighbor, cost in graph[curr_city]:
                if result[neighbor] > result[curr_city] + (k + 1) * cost:
                    result[neighbor] = result[curr_city] + (k + 1) * cost
                    heapq.heappush(heap, (result[neighbor], neighbor))

        return result       