# TLE
class Solution1:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        nums = [i if i else -1 for i in nums]
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]
        
        cnt = Counter()
        res = 0
        mod = 1000000007
        for i in range(n+1):
            cnt[presum[i]] += 1 
            res += sum([v for k, v in cnt.items() if k < presum[i]]) % mod
        return res % mod

class Solution2:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        
        def addOne(k):
            while k <= cap:
                cnt[k] += 1
                k += k & -k
        
        def rangeSum(k, res):
            while k:
                res += cnt[k]
                k -= k & -k
            return res % mod
        
        nums = [0] + [i if i else -1 for i in nums]
        n, cap, bot = len(nums), 0, 0
        for i in range(1, n):
            nums[i] += nums[i-1]
            if nums[i] < bot: bot = nums[i]
            if nums[i] > cap: cap = nums[i]
        
        add = -bot + 1   # shift presums to make presums start at 1 to fit BIT indexing
        cap += add
        cnt, res, mod = Counter(), 0, int(10**9+7)
        for i in range(n):
            k = nums[i] + add
            addOne(k)
            res = rangeSum(k-1, res)
            
        return res % mod

class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        # O(n)
        nums = [1 if i == 1 else -1 for i in nums]
        presum = [0] + nums
        for i in range(1, len(nums)+1):
            presum[i] += presum[i-1]
        mod = 1_000_000_007
        cnt = Counter()
        cnt[0] = 1
        c = 0
        res = 0
        for i in range(1, len(presum)):
            # c is count of subarrays ending at i which is broken down in following two cases (+1/-1):
            if presum[i] == presum[i-1] + 1:
                # count of subarrays of positive sum ending at i-1 + 
                # count of subarrays of 0 sum ending at i-1, including *empty array* (think about it)
                c += cnt[presum[i-1]] % mod
            else:  # presum[i] == presum[i-1] - 1:
                # count of subarrays of positive sum ending at i-1 - 
                # count of subarrays of 1 sum ending at i-1
                c -= cnt[presum[i-1]-1] % mod
            cnt[presum[i]] += 1
            res += c
        return res % mod