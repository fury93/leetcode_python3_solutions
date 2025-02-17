class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        ln = rows * cols
        res = [None] * ((ln + 1) // 2)
        i = 0

        while i < len(res):
            pos = i * 2
            curRow = pos // cols
            curCol = ~(pos % cols) if curRow & 1 else pos % cols
            res[i] = grid[curRow][curCol]
            i += 1

        return res
