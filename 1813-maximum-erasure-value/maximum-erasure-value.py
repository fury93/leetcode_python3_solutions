class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res, l, pos = 0, 0, defaultdict(lambda: -1)
        prefix = list(itertools.accumulate(nums, initial = 0))
        for r, ch in enumerate(nums):
            if pos[ch] >= l:
                l = pos[ch] + 1
            pos[ch] = r
            res = max(res, prefix[r+1] - prefix[l])
        
        return res
