class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def isBreak(str1, str2):
            for ch1, ch2 in zip(str1, str2):
                if ch1 < ch2: return False
            return True
        
        return isBreak(sorted(s1), sorted(s2)) \
            or isBreak(sorted(s2), sorted(s1))