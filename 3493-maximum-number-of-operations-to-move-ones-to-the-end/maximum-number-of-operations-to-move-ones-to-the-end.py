class Solution:
    def maxOperations(self, s: str) -> int:
        res, ones, lastId = 0, 0, len(s) - 1
        for i, ch in enumerate(s):
            if ch == '1':
                if i > 0 and s[i-1] == '0':
                    res += ones
                ones += 1     
            elif i == lastId and ch == '0':
                res += ones
        
        return res
        