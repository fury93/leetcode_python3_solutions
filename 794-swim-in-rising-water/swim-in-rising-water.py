class Solution:
    def swimInWater(self, grid):
        N, heap, visited, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        
        for i in range(N*N):
            val, x, y = heappop(heap)
            res = max(res, val)
            if x == N-1 and y == N-1: return res
            neib_list = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for dx, dy in neib_list:
                if (x + dx, y + dy) not in visited and 0<=x+dx<N and 0<=y+dy<N:
                    heappush(heap, (grid[x+dx][y+dy], x+dx, y+dy))
                    visited.add((x+dx, y+dy))