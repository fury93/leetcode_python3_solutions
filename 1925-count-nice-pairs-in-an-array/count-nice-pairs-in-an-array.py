class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        nums = [n - int(str(n)[::-1]) for n in nums]
        res = 0
        for n in Counter(nums).values():
            res += n*(n-1)//2 
        return res % (10**9 + 7)