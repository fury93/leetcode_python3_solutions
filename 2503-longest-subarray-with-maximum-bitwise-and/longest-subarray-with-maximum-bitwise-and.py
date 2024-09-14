class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxSubarrayLen, subarrayLen, mx, = 0, 0, max(nums)
        for n in nums:
            if n == mx:
                subarrayLen += 1
                maxSubarrayLen = max(maxSubarrayLen, subarrayLen)
            else:
                subarrayLen = 0
        
        return maxSubarrayLen