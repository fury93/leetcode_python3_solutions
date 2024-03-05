class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0, 0)]) # head - left, tail - right
        self.food = deque((x, y) for x, y in food)
        self.snakeCells = set((0, 0))
        self.w = width
        self.h = height

    def move(self, direction: str) -> int:
        row, col = self.snake[0]
        match direction:
            case 'R': col += 1
            case 'L': col -= 1
            case 'U': row -= 1
            case 'D': row += 1

        if not (0 <= row < self.h and 0 <= col < self.w):
            return -1 # border

        head = (row, col)
        if self.food and self.food[0] == head:
            self.food.popleft()
        else:
            self.snakeCells.discard(self.snake.pop())
        
        if head in self.snakeCells:
            return -1 # snake body already in this cell
        
        self.snake.appendleft(head)
        self.snakeCells.add(head)

        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)