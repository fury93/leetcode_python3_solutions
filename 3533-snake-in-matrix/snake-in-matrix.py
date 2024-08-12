class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row, col = 0, 0
        for c in commands:
            if c == 'UP':
                row -= 1
            elif c == 'DOWN':
                row += 1
            elif c == 'LEFT':
                col -= 1
            else:
                col += 1

        return row * n + col