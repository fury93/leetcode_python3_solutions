class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = Counter(digits)
        return sum(cnt >= Counter(map(int, str(n))) for n in range(100, 999, 2))