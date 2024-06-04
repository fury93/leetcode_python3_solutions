class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        for n in Counter(s).values():
            res += n if not n & 1 or not res & 1 else n-1

        return res