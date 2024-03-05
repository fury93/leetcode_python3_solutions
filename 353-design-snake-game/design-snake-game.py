class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.grid = [[None] * width for _ in range(height)]
        self.snake = deque([(0, 0)]) # head - most left, tail - most right
        self.food = deque(food)
        self.grid[0][0] = 1 # there is snake inumn this cell

    def move(self, direction: str) -> int:
        row, col = self.snake[0]
        match direction:
            case 'R': col += 1
            case 'L': col -= 1
            case 'U': row -= 1
            case 'D': row += 1

        if not (0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])):
            return -1 # border

        head = [row, col]
        if self.food and head == self.food[0]:
            self.food.popleft()
        else:
            row1, col1 = self.snake.pop() # remove tail
            self.grid[row1][col1] = None
        
        if self.grid[row][col] == 1:
            return -1 # snake body already in this cell
        
        self.snake.appendleft(head)
        self.grid[row][col] = 1

        return len(self.snake) - 1


        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)