class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        self.rows, self.cols, self.empty = len(rooms), len(rooms[0]), 2147483647
        q = deque()
        
        for row, col in product(range(self.rows), range(self.cols)):
            if rooms[row][col] == 0:
                q.append((row, col))
        
        while q:
            row, col = q.popleft()
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # right, down, left, up
                nextRow, nextCol = row + dy, col + dx
                if (
                    0 <= nextRow < self.rows and 
                    0 <= nextCol < self.cols and
                    rooms[nextRow][nextCol] == self.empty
                ):
                    rooms[nextRow][nextCol] = rooms[row][col] + 1
                    q.append((nextRow, nextCol))