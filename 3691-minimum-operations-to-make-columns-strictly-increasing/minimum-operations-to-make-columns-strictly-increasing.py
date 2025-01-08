class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        res = 0
        for col in zip(*grid):
            prev = -1
            for cur in col:
                if prev >= cur:
                    res += prev - cur + 1
                    cur = prev + 1
                prev = cur

        return res
        