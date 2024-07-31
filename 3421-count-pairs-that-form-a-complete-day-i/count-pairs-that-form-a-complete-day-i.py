class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        freq = Counter(h % 24 for h in hours)
        
        res = 0
        for h1 in freq:
            h2 = (24 - h1) % 24
            if h2 not in freq or h1 < h2: continue
            if h1 != h2:
                res += freq[h1] * freq[h2]
            else: 
                res += freq[h1] * (freq[h1] - 1) // 2

        return res
        