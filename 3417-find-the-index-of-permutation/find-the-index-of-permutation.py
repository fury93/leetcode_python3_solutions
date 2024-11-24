class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        smaller_to_right = [0] * len(perm)

        def merge(left, right):
            if left >= right: return [left]

            mid = left + right >> 1
            l_nums, r_nums = merge(left, mid), merge(mid + 1, right)
            merged, p_l, p_r = [], 0, 0

            while p_l < len(l_nums) or p_r < len(r_nums):
                if p_r == len(r_nums) or (p_l < len(l_nums) and perm[l_nums[p_l]] < perm[r_nums[p_r]]):
                    smaller_to_right[l_nums[p_l]] += p_r
                    merged.append(l_nums[p_l])
                    p_l += 1
                else:
                    merged.append(r_nums[p_r])
                    p_r += 1
            
            return merged
        
        merge(0, len(perm) - 1)

        MOD = 10 ** 9 + 7
        fact = [1, 1]
        for i in range(2, len(perm) + 1):
            fact.append(fact[-1] * i % MOD)
        
        return sum(smaller_to_right[i] * fact[len(perm) - i - 1] % MOD for i in range(len(perm))) % MOD