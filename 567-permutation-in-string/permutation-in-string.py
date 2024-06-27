class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        
        need, matched = Counter(s1), 0

        for i, ch in enumerate(s2, start = 1):
            if ch in need:
                matched += need[ch] > 0
                need[ch] -= 1
            
            if i < len(s1): continue

            if matched == len(s1): return True

            removeCh = s2[i - len(s1)]
            if removeCh in need:
                need[removeCh] += 1
                matched -= need[removeCh] > 0

        return False
    
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        L, l = len(s1)-1, 0
        cnt1, cnt2 = Counter(s1), Counter(s2[:L])

        for r, c in enumerate(s2[L:]):
            cnt2[c] += 1
            if cnt1 == cnt2: return True
            cnt2[s2[l]] -= 1
            l += 1

        return False
