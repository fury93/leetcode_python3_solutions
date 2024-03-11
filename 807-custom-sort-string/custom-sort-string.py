class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {v:k for k, v in enumerate(order)}
        return ''.join(sorted(s, key=lambda ch: d[ch] if ch in d else len(s)))