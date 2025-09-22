class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        maxFreq = max(cnt.values())

        return maxFreq * sum(freq == maxFreq for freq in cnt.values())