class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, q, fresh, R, C = 0, deque(), 0,  len(grid), len(grid[0])

        for x, y in product(range(R), range(C)):
            if grid[x][y] == 2:
                q.append((x, y))
            elif grid[x][y] == 1:
                fresh += 1
        
        while q and fresh > 0:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < R and 0 <= yy < C and grid[xx][yy] == 1:
                        grid[xx][yy] = 2
                        fresh -= 1
                        q.append((xx, yy))
            time += 1

        return time if not fresh else - 1



    def orangesRotting2(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting: return -1
            rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
            fresh -= rotting
            timer += 1
        return timer