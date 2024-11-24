class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        # Sequence of pairs (idx, gcd), both strictly increasing.
        gcds = []
        prefix_sum = [0]
        best = 0
        for i, x in enumerate(nums):
            prefix_sum.append(prefix_sum[-1] + x)
            new_gcds = []
            for j, g in gcds + [(i, x)]:
                ng = gcd(g, x)
                # Skipping duplicates.
                if not new_gcds or new_gcds[-1][1] != ng:
                    new_gcds.append((j, ng))
            gcds = new_gcds
            for j, g in gcds:
                if i - j + 1 < k: break
                best = max(best, (prefix_sum[-1] - prefix_sum[j]) * g)
        return best

        