class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        l1 = [0]*5001
        l2 = [0]*5001
        
        def query(l, price):
            m = 0
            while price:
                m = max(m, l[price])
                price &= price - 1
            return m
        
        def update(l, price, val):
            while price < 5001:
                l[price] = max(l[price], val)
                price += price & (-price)
        
        m = -1
        for price, profit in zip(prices, profits):
            tmp1 = query(l1, price-1)
            tmp2 = query(l2, price-1)
            if tmp2:
                m = max(m, tmp2 + profit)
            update(l1, price, profit)
            if tmp1:
                update(l2, price, profit+tmp1)
        return m