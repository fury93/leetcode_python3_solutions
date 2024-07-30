class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(bool(n % 3) for n in nums)