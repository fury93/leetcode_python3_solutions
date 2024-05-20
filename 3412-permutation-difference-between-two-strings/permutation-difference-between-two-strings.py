class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = {ch: pos for pos, ch in enumerate(s)}
        
        return sum(abs(pos - d[ch]) for pos, ch in enumerate(t))