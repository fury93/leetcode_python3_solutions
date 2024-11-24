class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        from math import gcd
        all_nums = set(range(1, n + 1))
        self.output = 0

        def backtrack(path, N):
            if len(path) == n:
                self.output += 1
            else:
                for num in all_nums:
                    if num not in path and gcd(num, N) == 1:
                        backtrack(path + [num], N + 1)

        backtrack([], 1)
        return self.output

