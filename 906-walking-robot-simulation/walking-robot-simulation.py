class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(tuple(_) for _ in obstacles)
        res, curX, curY, diffX, diffY  = 0, 0, 0, 0, 1

        for command in commands:
            if command < 0: #change direction 
                match command:
                    case -1: diffX, diffY = diffY, -diffX # clockwise
                    case -2: diffX, diffY = -diffY, diffX # anti-clockwise
                continue
            
            for _ in range(command):
                nextX, nextY = curX + diffX, curY + diffY
                if (nextX, nextY) in obstacles: break
                curX, curY = nextX, nextY
            
            res = max(res, curX*curX + curY*curY)

        return res
