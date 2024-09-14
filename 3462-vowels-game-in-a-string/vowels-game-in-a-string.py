class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set(['a', 'e', 'u', 'i', 'o'])
        cntVowels = sum(ch in vowels for ch in s)
        return cntVowels > 0