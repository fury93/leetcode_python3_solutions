class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        
        if sum(cnt & 1 for cnt in freq) > 1: return []

        singleChar = ''
        for i, cnt in enumerate(freq):
            if cnt & 1:
                singleChar = chr(i + 97)
            freq[i] = cnt // 2 # remove half of symbols
        
        res, maxLen = [], sum(freq)

        def backtrack(perm):
            if len(perm) == maxLen:
                palindrome = ''.join(perm + [singleChar] + perm[::-1])
                res.append(palindrome)
                return
            
            for i in range(len(freq)):
                if freq[i] > 0:
                    perm.append(chr(i + 97))
                    freq[i] -= 1
                    backtrack(perm)
                    perm.pop()
                    freq[i] += 1

        backtrack([])

        return res