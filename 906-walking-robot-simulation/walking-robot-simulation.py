class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set((x, y) for x, y in obstacles)
        res, curPosition, curDirection  = 0, (0, 0), 0
        #if (0, 0) in obstacles: return res # this test-case doesn't work
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # north, east, south, west

        for command in commands:
            if command < 0: #change direction command
                match command:
                    case -1: curDirection += 1
                    case -2: curDirection -= 1
                curDirection %= len(direction)
                continue
            
            for _ in range(command):
                # nextPosition = tuple(pos + diff for pos, diff in zip(curPosition, direction[curDirection]))
                nextPosition = (curPosition[0] + direction[curDirection][0], curPosition[1] + direction[curDirection][1])
                if nextPosition in obstacles:
                    break
                curPosition = nextPosition
            
            #res = max(res, curPosition[0]**2 + curPosition[1]**2)
            res = max(res, sum(map(lambda x: x*x, curPosition)))

        return res
