class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        nextExpectedValue = 1
        coins.sort()

        for coin in coins:
            if coin <= nextExpectedValue:
                nextExpectedValue += coin
            else: break

        return nextExpectedValue
