class Solution:
    def residuePrefixes(self, s: str) -> int:
        return sum(len(set(s[:i])) == i % 3 for i in range(1, len(s)+1))