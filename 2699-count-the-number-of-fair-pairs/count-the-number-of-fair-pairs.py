class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res, ln = 0, len(nums)
        for i, n in enumerate(nums):
            left = min(bisect_left(nums, lower - n, i + 1), ln)
            right = bisect_right(nums, upper - n, i + 1)
            res += right - left

        return res