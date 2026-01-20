class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def getPrimes(limit):
            primes = [True] * (limit + 1)
            primes[0] = primes[1] = False
            
            for p in range(2, int(limit**0.5) + 1):
                if primes[p]:
                    for i in range(p * p, limit + 1, p):
                        primes[i] = False
            
            return [val for val, isPrime in enumerate(primes) if isPrime]

        res, primes = [], getPrimes(n)
        l, r = 0, len(primes) - 1

        while l <= r:
            sm = primes[l] + primes[r]
            if sm < n:
                l += 1
            elif sm > n:
                r -= 1
            else:
                res.append([primes[l], primes[r]])
                l += 1
                r -= 1
        
        return res