class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0] * 101
        for n in nums:
            cnt[n] += 1
        cnt = list(accumulate(cnt, initial = 0))

        return [cnt[n] for n in nums]
            

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        d = {}
        for id, n in enumerate(sorted(nums)):
            d.setdefault(n, id) #if n not in d
        
        return [d[n] for n in nums]
