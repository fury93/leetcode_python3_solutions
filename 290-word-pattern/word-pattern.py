class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))

    def wordPattern2(self, pattern: str, s: str) -> bool:
        dic1, dic2 = {}, {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for c, word in zip(pattern, words):
            if c not in dic1 and word not in dic2:
                dic1[c] = word
                dic2[word] = c
            elif dic1.get(c) != word or dic2.get(word) != c:
                return False
        return True
            