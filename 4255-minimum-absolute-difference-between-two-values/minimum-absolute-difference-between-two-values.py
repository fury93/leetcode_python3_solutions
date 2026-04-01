class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        res, prevPos = len(nums), None
        for i, n in enumerate(nums):
            if n == 0: continue
            if prevPos is not None and n != nums[prevPos]:
                res = min(res, abs(i - prevPos))
            prevPos = i

        return -1 if res == len(nums) else res

