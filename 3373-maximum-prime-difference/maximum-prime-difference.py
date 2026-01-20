class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def getPrimes(limit):
            primes = [True] * (limit + 1)
            primes[0] = primes[1] = False
            
            for p in range(2, int(limit**0.5) + 1):
                if primes[p]:
                    for i in range(p * p, limit + 1, p):
                        primes[i] = False
            return primes
    
        primes = getPrimes(100)
        
        l ,r = 0, len(nums) - 1
        while l < len(nums) and not primes[nums[l]]:
            l += 1
        while r >= 0 and not primes[nums[r]]:
            r -= 1

        return r - l
        