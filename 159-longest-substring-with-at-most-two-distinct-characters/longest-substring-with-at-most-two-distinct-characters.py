class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res, pos, l = 0, defaultdict(int), 0
        for r, ch in enumerate(s):
            pos[ch] = r
            if len(pos) > 2:
                removeCh = min(pos, key=pos.get)
                l = pos[removeCh] + 1
                del pos[removeCh]
            res = max(res, r - l + 1)
        return res