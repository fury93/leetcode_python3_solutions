class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if start == destination: return True
        
        rows, cols, processed = len(maze), len(maze[0]), -1
        q = deque([start])

        while q:
            r, c = q.popleft() # r - rows, c - cols
            #print('start', r, c, q)

            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                rr, cc = r + dr, c + dc
                while 0 <= rr < rows and 0 <= cc < cols and maze[rr][cc] != 1:
                    rr, cc = rr + dr, cc + dc
                rr, cc = rr - dr, cc - dc # how to get rid of this line ?
                #print(rr, cc)

                if rr == destination[0] and cc == destination[1]: return True
                if maze[rr][cc] == 0:
                    q.append((rr, cc))
            
            maze[r][c] = processed
                

        return False


