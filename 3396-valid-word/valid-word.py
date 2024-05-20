class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 or not word.isalnum(): return False
        
        isVowel, isConsonant = False, False,
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        for ch in word:
            if ch.isalpha():
                if ch.lower() in vowels:
                    isVowel = True
                else:
                    isConsonant = True
        
        return isVowel and isConsonant