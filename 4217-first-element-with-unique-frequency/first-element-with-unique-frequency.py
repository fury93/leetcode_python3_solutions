class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        uniqFreq = [k for k, v in Counter(cnt.values()).items() if v == 1]
        for n in nums:
            if cnt[n] in uniqFreq: return n
        return -1