class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res, l, freq = 0, 0, defaultdict(int)

        for r, num in enumerate(nums):
            freq[num] += 1
            while freq[num] > k:
                freq[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res 
