class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return sum(n * (n+1) // 2 for n in Counter(s).values())