class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            n_str = str(n)
            maxDig = max(n_str)
            res += int(len(n_str) * maxDig)
        return res