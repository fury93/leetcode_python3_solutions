class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set((x, y) for x, y in obstacles)
        res, curPosition, curDirection  = 0, (0, 0), 0
        #if (0, 0) in obstacles:
              #print('stop')
        #     return res
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # north, east, south, west

        for command in commands:
            if command < 0: #change direction command
                match command:
                    case -1: curDirection += 1
                    case -2: curDirection -= 1
                curDirection %= len(direction)
                continue
            
            for step in range(command):
                nextPosition = tuple(pos + diff for pos, diff in zip(curPosition, direction[curDirection]))
                if nextPosition in obstacles:
                    break
                curPosition = nextPosition
            
            res = max(res, curPosition[0]**2 + curPosition[1]**2)

        return res
