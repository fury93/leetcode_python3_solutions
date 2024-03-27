class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        res, product, l, r = 0, 1, 0, 0
        while r < len(nums):
            product *= nums[r]
            while product >= k:
                product /= nums[l]
                l +=1
            res += r - l + 1
            r+=1
        
        return res