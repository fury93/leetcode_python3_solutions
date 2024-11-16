class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums

        res, power = [-1] * (len(nums) - k + 1), 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] + 1:
                power += 1
            else:
                power = 1

            if power >= k:
                res[i - k + 1] = nums[i]

        return res