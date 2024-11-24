class Solution:
    def maxSubstringLength(self, s: str) -> int:
        cnts = Counter(s)
        
        prefix = [[0 for char in range(26)] for i in range(len(s)+1)]
        rMost = {}
        lMost = {}
        ans = 0
        for i in range(1, len(s)+1):
            char = s[i-1]
            if char not in lMost:
                lMost[char] = i
            rMost[char] = i
            prefix[i][ord(char) - ord("a")] += 1
            for freq in range(26):
                prefix[i][freq] += prefix[i-1][freq]
        
    
        for char in lMost:
            left = lMost[char]
            for c2 in rMost:
                right = rMost[c2]
                if (right == len(s) and left == 1) or (right < left):
                    continue
                valid = True
                for i, (rfreq, lfreq) in enumerate(zip(prefix[right], prefix[left-1])):
                    if rfreq-lfreq != 0 and rfreq-lfreq != cnts[chr(i + ord("a"))]:
                        valid = False
                        break
                if valid:
                    ans = max(ans, right-left+1)
        return ans if ans != 0 else -1