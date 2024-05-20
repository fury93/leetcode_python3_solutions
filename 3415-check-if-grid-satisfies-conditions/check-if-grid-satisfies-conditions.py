class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for coll in zip(*grid):
            prev = coll[0]
            for cell in coll:
                if cell != prev:
                    return False

        prev = None
        for cell in grid[0]:
            if cell == prev:
                return False
            prev = cell

        return True
