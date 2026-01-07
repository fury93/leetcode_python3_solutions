# Dijkstra
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        visited = [[rows + cols + 1] * cols for _ in range(rows)]

        while pq:
            h, r, c = heappop(pq)
            if visited[r][c] < h: continue

            if r == rows - 1 and c == cols - 1:
                return h < health

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    nh = h + grid[nr][nc]
                    if nh < health and nh < visited[nr][nc]:
                        visited[nr][nc] = nh
                        heappush(pq, (nh, nr, nc))

        return False