class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res, ROWS, COLS = [], len(land), len(land[0])
        
        def dfs(r, c):
            maxRightDown = (r, c)
            land[r][c] = 0
            for dr, dc in [(0, 1), (1, 0)]:
                rr, cc = r + dr, c + dc
                if rr < ROWS and cc < COLS and land[rr][cc] == 1:
                    maxRightDown = max(dfs(rr, cc), maxRightDown)
            return maxRightDown 

        for r, c in product(range(ROWS), range(COLS)):
            if land[r][c] == 1:
                r2, c2 = dfs(r, c)
                res.append([r, c, r2, c2])
        
        return res