class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        res = -math.inf
        prefix, suffix = 0, sum(nums)
        for n in nums:
            prefix += n
            res = max(res, prefix, suffix)
            suffix -= n

        return res

class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        ans = -sys.maxsize
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        s = prefix[-1]    
        for i, num in enumerate(nums):
            cur = max(prefix[i+1], s-prefix[i+1]+num)
            ans = max(ans, cur)
        return ans