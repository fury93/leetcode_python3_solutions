class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res, uf = [], UnionFind(m , n)
        for row, col in positions:
            uf.add(row, col)
            for rowDiff, colDiff in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                adjacentRow, adjacentCol = row + rowDiff, col + colDiff
                if 0 <= adjacentRow < m and 0 <= adjacentCol < n:
                    uf.union(row, col, adjacentRow, adjacentCol)
            res.append(uf.count())
                    
        return res

class UnionFind:
    def __init__(self, rows, cols):
        size = rows * cols
        self.root = [None for i in range(size)]
        self.rank = [0] * size
        self.cnt = 0
        self.rowSize = cols

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, row1, col1, row2, col2):
        idx1, idx2 = self.getIdx(row1, col1), self.getIdx(row2, col2)
        if not self.exist(idx1) or not self.exist(idx2): return

        rootX = self.find(idx1)
        rootY = self.find(idx2)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.cnt -= 1

    def getIdx(self, row, col):
        return row * self.rowSize + col

    def add(self, row, col):
        idx = self.getIdx(row, col)
        if not self.exist(idx):
            self.root[idx] = idx
            self.rank[idx] = 1
            self.cnt += 1

    def count(self):
        return self.cnt

    def exist(self, idx):
        print(idx)
        return self.root[idx] is not None