class Solution:
    #prefixSum[j] - prefixSum[i] = k => prefixSum[j] - k = prefixSum[i]
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res, pos, sm = 0, {0: -1}, 0
        for i, n in enumerate(nums):
            sm += n
            if sm not in pos:
                pos[sm] = i
            if sm - k in pos:
                res = max(res, i - pos[sm-k])
        return res
