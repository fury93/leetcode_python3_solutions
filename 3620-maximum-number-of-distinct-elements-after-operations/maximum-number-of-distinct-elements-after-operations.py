class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        res, maxUniq = 0, - math.inf
        nums.sort()

        for n in nums:
            if maxUniq > n + k: continue
            nextMaxUniq = max(maxUniq + 1, n - k)

            if n - k <= nextMaxUniq <= n + k:
                res += 1
                maxUniq = nextMaxUniq

        return res