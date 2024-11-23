class Solution:
    def countLetters(self, s: str) -> int:
        sm = 0
        for _, g in groupby(s):
            ln = len(list(g))
            sm += ln * (ln + 1) //2
        return sm