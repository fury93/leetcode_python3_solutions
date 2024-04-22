class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res, ds = [], UnionFind()
        for x, y in positions:
            ds.add((x, y))
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                xx, yy = x + dx, y + dy
                if ds.isExist((xx, yy)):
                    ds.union((xx, yy), (x, y))
            res.append(ds.getCnt())
                    
        return res

class UnionFind:
    def __init__(self):
        self.root = dict()
        self.rank = dict()
        self.cnt = 0

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.cnt -= 1

    def add(self, key):
        if key in self.root: return
        self.root[key] = key
        self.rank[key] = 1
        self.cnt += 1

    def getCnt(self):
        return self.cnt

    def isExist(self, key):
        return key in self.root