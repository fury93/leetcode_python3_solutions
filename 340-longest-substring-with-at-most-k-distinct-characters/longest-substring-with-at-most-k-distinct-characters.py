class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
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
