class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            remainder = n % 3
            if remainder != 0:
                res += min(remainder, 3 - remainder)

        return res