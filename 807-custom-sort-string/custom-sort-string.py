class Solution:
    def customSortString2(self, order: str, s: str) -> str:
        d = {v:k for k, v in enumerate(order)}
        return ''.join(sorted(s, key=lambda ch: d[ch] if ch in d else len(s)))

    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        chars1 = [ch * cnt[ch] for ch in order]
        chars2 = [ch * cnt for ch, cnt in cnt.items() if ch not in order]
        return ''.join(chain(chars1, chars2))