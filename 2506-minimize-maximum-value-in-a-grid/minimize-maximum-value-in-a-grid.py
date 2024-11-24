class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        vals = [(grid[i][j],i,j) for i in range(m) for j in range(n)]
        row_max,col_max = [0]*m,[0]*n
        for _,i,j in sorted(vals):
            v = max(row_max[i],col_max[j])+1
            row_max[i],col_max[j]=v,v
            grid[i][j]=v
        return grid