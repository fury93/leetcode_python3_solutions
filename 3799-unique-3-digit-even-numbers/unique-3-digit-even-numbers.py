class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        numbers = set()

        for a, b, c in permutations(digits, 3):
            if c % 2 == 0 and a != 0:
                numbers.add((a, b, c))

        return len(numbers)

    def totalNumbers2(self, digits: List[int]) -> int:
        cnt = Counter(map(str, digits))
        return sum(cnt >= Counter(str(n)) for n in range(100, 1000, 2))