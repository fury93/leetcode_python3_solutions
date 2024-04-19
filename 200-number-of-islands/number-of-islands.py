from itertools import product
class Solution:
    L = '1'
    W = '0'

    def numIslands(self, grid: List[List[str]]) -> int:
        res, R, C = 0, len(grid), len(grid[0])

        def dfs(x, y):
            if 0 <= x < R and 0 <= y < C and grid[x][y] == self.L:
                grid[x][y] = self.W
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    dfs(x + dx, y + dy)

        for i, j in product(range(R), range(C)):
                if grid[i][j] == self.L:
                    res += 1
                    dfs(i, j)

        return res

