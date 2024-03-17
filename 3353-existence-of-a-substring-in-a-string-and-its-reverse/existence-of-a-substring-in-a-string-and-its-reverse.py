class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i] == s[i-1] or i + 1 < len(s) and s[i-1] == s[i+1]:
                return True
        return False