class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        res = 0
        for holes in sorted(map(len, road.split('.')), reverse=True):
            res += min(holes, max(0, budget - 1))
            budget -= min(holes + 1, budget)
        return res