class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        R = C = len(grid)
        q = deque((r, c, 0) for r, c in product(range(R), range(C)) if grid[r][c] == 1)
        if len(q) == R * C or len(q) == 0:
            return -1
        
        res = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            r, c, d = q.popleft()
            for dr, dc in directions:
                nr, nc, nd = r + dr, c + dc, d + 1
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                    grid[nr][nc] = nd
                    q.append((nr, nc, nd))
                    res = max(res, grid[nr][nc])
        
        return res