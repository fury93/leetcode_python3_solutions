class Solution:
    def minOperations(self, nums: list[int], x: int, y: int) -> int:
        def predicate(ops: int) -> bool:
            return sum(max(0, math.ceil((num - ops * y) / (x - y)))
                       for num in nums) <= ops

        return bisect.bisect_left(range(max(nums)), True, key=predicate)