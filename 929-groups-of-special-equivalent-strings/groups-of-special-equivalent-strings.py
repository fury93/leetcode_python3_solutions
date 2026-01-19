class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()
        for w in words:
            even = ''.join(sorted(w[::2]))
            odd = ''.join(sorted(w[1::2]))
            groups.add((even, odd))
        return len(groups)

