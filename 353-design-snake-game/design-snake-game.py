class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0, 0)]) # head - left, tail - right, used for the order
        self.snakeCells = set((0, 0)) # use for fast search if current cell busy with the snake body
        self.food = deque((x, y) for x, y in food) # I prefere to use tuples for coordinats
        self.w = width
        self.h = height

    def move(self, direction: str) -> int:
        # 1. Make new move, it's new head position
        row, col = self.snake[0]
        match direction:
            case 'R': col += 1
            case 'L': col -= 1
            case 'U': row -= 1
            case 'D': row += 1

        # 2. Check if head doesn't go out of bounds (hits a wall)
        if not (0 <= row < self.h and 0 <= col < self.w): return -1 

        head = (row, col)
        # 3. If a food in the head cell => remove this food and leave old tail
        # 4. Else remove old tail, it will be moved to new head cell later
        if self.food and self.food[0] == head:
            self.food.popleft()
        else:
            self.snakeCells.discard(self.snake.pop())
        
        # 5. check if new head don't cross the snake body
        if head in self.snakeCells: return -1
        
        # 6. Add new head 
        self.snake.appendleft(head)
        self.snakeCells.add(head)

        # 7. Score equal to the snake size without the head
        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)