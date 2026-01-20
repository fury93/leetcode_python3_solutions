class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        for row, limit in zip(grid, limits):
            candidates.extend(sorted(row, reverse = True)[:limit])
        
        return sum(sorted(candidates, reverse = True)[:k])