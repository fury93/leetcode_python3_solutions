class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        uniq = set(key for key in cnt if cnt[key] == 1)
        if k == 1:
            return max(uniq, default = -1)
        if k == len(nums):
            return max(nums)
        
        if k == 1:
            return max(nums)
        
        cnt1 = nums.count(nums[0])
        cnt2 = nums.count(nums[-1])

        if cnt1 > 1:
            return -1 if cnt2 > 1 else nums[-1]

        return nums[0] if cnt2 > 1 else max(nums[0], nums[-1])