class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        def getCost(logSize, maxSize):
            cost = 0
            while logSize > maxSize:
                logSize = logSize - maxSize
                cost += logSize * maxSize
            return cost
        
        return getCost(n, k) + getCost(m, k)