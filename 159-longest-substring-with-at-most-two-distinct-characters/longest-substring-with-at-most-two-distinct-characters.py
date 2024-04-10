class Solution:
    def lengthOfLongestSubstringTwoDistinct2(self, s: str) -> int:
        res, pos, l = 0, defaultdict(int), 0
        for r, ch in enumerate(s):
            pos[ch] = r
            if len(pos) > 2:
                removeCh = min(pos, key=pos.get)
                l = pos[removeCh] + 1
                del pos[removeCh]
            res = max(res, r - l + 1)
        return res

    def lengthOfLongestSubstringTwoDistinct(self, s: str, k = 2) -> int:
        d, l, = defaultdict(int), 0
        for r, ch in enumerate(s):
            d[ch] += 1
            if len(d) > k:
                removeCh = s[l]
                d[removeCh] -= 1
                if d[removeCh] == 0:
                    del d[removeCh]
                l += 1
        
        return r - l + 1