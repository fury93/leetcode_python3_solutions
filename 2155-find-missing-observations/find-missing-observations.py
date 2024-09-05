class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        expectedSum = (len(rolls) + n) * mean - sum(rolls)
        if expectedSum < n or expectedSum > n * 6:
            return []

        quotient, remainder  = divmod(expectedSum, n)
        return [quotient + 1] * remainder + [quotient] * (n - remainder)