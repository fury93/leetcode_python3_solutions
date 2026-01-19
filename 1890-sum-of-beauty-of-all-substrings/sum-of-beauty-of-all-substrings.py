# O(N^2)
class Solution:
    def beautySum(self, s: str) -> int:
        res, freq = 0, defaultdict(int)
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - 97] += 1
                vals = [val for val in freq if val > 0]
                res += max(vals) - min(vals)
        return res
