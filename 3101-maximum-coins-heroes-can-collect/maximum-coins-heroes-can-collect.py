class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        monsters, coins = zip(*sorted(zip(monsters, coins), key = lambda x: x[0]))
        coins = list(accumulate(coins, initial = 0))
        return [coins[bisect_right(monsters, power)] for power in heroes]
        res = [0] * len(heroes)
        for i, power in enumerate(heroes):
            pos = bisect_right(monsters, power)
            if pos > 0:
                res[i] = coins[pos-1]
        
        return res