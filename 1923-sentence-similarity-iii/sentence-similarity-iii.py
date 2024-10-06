class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) > len(sentence2):
            return self.areSentencesSimilar(sentence2, sentence1)
        
        s1 = sentence1.split()
        s2 = sentence2.split()
        
        i = 0
        while i < len(s1) and s1[i] == s2[i]:
            i += 1
        
        if i == len(s1): return True
        
        j = len(s2) - 1
        while j > i and s1[i] != s2[j]:
            j -= 1
        
        while i < len(s1) and j < len(s2) and s1[i] == s2[j]:
            i += 1
            j += 1
        
        return i == len(s1) and j == len(s2)
