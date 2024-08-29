# the same https://leetcode.com/problems/maximum-array-hopping-score-i/
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        res, maxN = 0, 0
        for i in range(len(nums)-1, 0, -1):
            maxN = max(maxN, nums[i])
            res += maxN

        return res