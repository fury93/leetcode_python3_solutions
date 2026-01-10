class Solution:
    def scoreBalance(self, s: str) -> bool:
        weights = [ord(ch) - 96 for ch in s]
        scores = list(accumulate(weights))
        return not scores[-1] & 1 and scores[-1]//2 in scores