class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        max_sum = pos = nes = float('-inf')
        for i, num in enumerate(nums):
            pos, nes = max(nes + num, num), pos - num
            max_sum = max(max_sum, pos, nes)
        return max_sum