class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = [[] for _ in range(n)]
        for u, v, price in flights:
            adjList[u].append((v, price))
        
        # stops = -1 because on the next 1'st layer won't be any stops between 2 cities, stops = 0
        # with k stops there are maximum (k + 1) cities 
        q = [(0, k + 1, src)] # price, stops, city.
        visited = set() # pair of (city, stops)

        while q:
            price, stops, city = heappop(q)
            if (city, stops) in visited: continue
            
            if city == dst:
                return price

            visited.add((city, stops))
            stops -= 1
            if stops < 0: continue # no more stops is availabe

            for nextCity, flyCost in adjList[city]:
                if (nextCity, stops) not in visited:
                    heappush(q, (price + flyCost, stops, nextCity))

        return -1

    def findCheapestPrice2(self, n, flights, src, dst, k):
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
        
        # (price, stops, city)
        pq = [(0, 0, src)] 
        
        # Храним лучшее количество остановок для достижения города
        best_stops = {} 

        while pq:
            price, stops, city = heapq.heappop(pq)
            
            if city == dst:
                return price
            
            # Если мы превысили лимит остановок, пропускаем этот путь
            if stops > k:
                continue
                
            # Оптимизация: если мы уже нашли лучший путь (с меньшим кол-вом остановок), пропускаем
            if city in best_stops and best_stops[city] <= stops:
                continue
            best_stops[city] = stops


            for nextCity, flyCost in adj[city]:
                heapq.heappush(pq, (price + flyCost, stops + 1, nextCity))

        return -1


    def findCheapestPrice4(self, n, flights, src, dst, k):
        dist = [float('inf')] * n
        dist[src] = 0
        
        # K остановок = K+1 перелет(ребро)
        for _ in range(k + 1):
            tmp = dist[:] # Копируем текущие лучшие цены
            for u, v, w in flights:
                # Если до src добрались
                if dist[u] != float('inf'):
                    # Пытаемся улучшить путь до dst, используя 1 ребро
                    tmp[v] = min(tmp[v], dist[u] + w)
            dist = tmp # Обновляем основной массив
            
        return dist[dst] if dist[dst] != float('inf') else -1


    def findCheapestPrice3(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, price in flights:
            adjList[u].append((v, price))
        
        # prices[i] хранит минимальную цену для достижения города i с текущим числом остановок
        prices = [math.inf] * n
        prices[src] = 0
        
        q = deque([(src, 0)]) # (city, current_price)
        stops = 0
        
        while q and stops <= k:
            # Обрабатываем все города на текущем уровне остановок
            for _ in range(len(q)):
                u, current_price = q.popleft()
                
                for v, flyCost in adjList[u]:
                    new_price = current_price + flyCost
                    
                    # Если новый путь дешевле, обновляем цену и добавляем в очередь
                    if new_price < prices[v]:
                        prices[v] = new_price
                        q.append((v, new_price))
            
            stops += 1 # Переходим на следующий уровень (добавляем 1 остановку)
            
        return prices[dst] if prices[dst] != math.inf else -1