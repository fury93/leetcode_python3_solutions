class Solution:
    def minOperations(self, nums: List[int]) -> int:
        @cache
        def getLowestFactor(n):
            if n % 2 == 0: return 2

            for d in range(3, math.isqrt(n)+1, 1):
                if n % d == 0:
                     return d

            return n

        res = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                nums[i] = getLowestFactor(nums[i])
                if nums[i] > nums[i+1]:
                    return -1
                res += 1

        return res