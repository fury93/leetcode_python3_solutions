class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minN, maxN, minNPos, maxNPos = math.inf, -math.inf, None, None
        for pos, n in enumerate(nums):
            if n < minN:
                minN, minNPos = n, pos
            if n >= maxN:
                maxN, maxNPos = n ,pos
        doubleSwap = 1 if maxNPos < minNPos else 0
        
        return minNPos + len(nums) - 1 - maxNPos - doubleSwap   

