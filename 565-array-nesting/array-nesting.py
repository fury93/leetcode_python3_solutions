class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        maxLen = 0
        for i, n in enumerate(nums):
            curLen = 0
            while nums[i] >= 0:
                ii = nums[i]
                nums[i] = -1
                i = ii
                curLen += 1
            maxLen = max(maxLen, curLen)

        return maxLen