class Solution:
    def isThereAPath(self, grid: list[list[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        if (rows + cols) % 2 == 0:
            return False

        min_ = [[0] * cols for _ in range(rows)]
        max_ = [[0] * cols for _ in range(rows)]

        min_[0][0] = max_[0][0] = grid[0][0]

        for row in range(1, rows):
            min_[row][0] = min_[row - 1][0] + grid[row][0]
            max_[row][0] = max_[row - 1][0] + grid[row][0]

        for col in range(1, cols):
            min_[0][col] = min_[0][col - 1] + grid[0][col]
            max_[0][col] = max_[0][col - 1] + grid[0][col]

        for row in range(1, rows):
            for col in range(1, cols):
                min_prev = min(min_[row - 1][col], min_[row][col - 1])
                min_[row][col] = min_prev + grid[row][col]

                max_prev = max(max_[row - 1][col], max_[row][col - 1])
                max_[row][col] = max_prev + grid[row][col]

        target = (rows + cols - 1) // 2
        return min_[rows - 1][cols - 1] <= target <= max_[rows - 1][cols - 1]