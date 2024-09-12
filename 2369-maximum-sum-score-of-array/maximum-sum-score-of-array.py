class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        res = -math.inf
        prefix, suffix = 0, sum(nums)
        for n in nums:
            prefix += n
            res = max(res, prefix, suffix)
            suffix -= n

        return res