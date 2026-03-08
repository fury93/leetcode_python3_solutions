class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0: return False
        R, C = len(grid), len(grid[0])
        moves = [None] * (R * C)

        for r, c in product(range(R), range(C)):
            moves[grid[r][c]] = (r, c)

        for prev, cur in pairwise(moves):
            if abs(prev[0] - cur[0]) *  abs(prev[1] - cur[1]) != 2:
                return False

        return True
