class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        beforePrev = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            prev, beforePrev = max(prev, beforePrev + nums[i]), prev

        return prev
    
    # Bottom-up without optimization
    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        money = [None] * len(nums)
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            money[i] = max(money[i-1], money[i-2] + nums[i])

        return money[-1]