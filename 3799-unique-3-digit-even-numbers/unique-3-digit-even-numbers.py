class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = Counter(map(str, digits))
        return sum(cnt >= Counter(str(n)) for n in range(100, 1000, 2))