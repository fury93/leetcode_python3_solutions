class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr = dict()
        for w in dictionary:
            key = self.convertToAbbr(w)
            if key in self.abbr and self.abbr[key] != w:
                self.abbr[key] = ''
            else:
                self.abbr[key] = w

    def isUnique(self, word: str) -> bool:
        key = self.convertToAbbr(word)
        return not key in self.abbr or self.abbr[key] == word

    def convertToAbbr(self, w):
        return w if (ln:=len(w)) < 2 else f'{w[0]}{ln-2}{w[-1]}'