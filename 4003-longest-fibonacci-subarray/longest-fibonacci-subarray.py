class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, ln = 0, 0
        for i in range(2, len(nums)):
            if nums[i] == nums[i-1] + nums[i-2]:
                ln += 1
            else:
                ln = 0
            res = max(res, ln)
        return res + 2