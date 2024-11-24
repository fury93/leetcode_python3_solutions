class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        mod = 10**9 + 7
        pre_sum_array = defaultdict()
        
        big_y_pairs = {(xi, yi) for xi, yi in queries if yi > sqrt(n)}
        big_y_pair_sums = {(xi, yi): sum(nums[xi: n: yi]) for xi, yi in big_y_pairs}
        
        pre_sum_array_keys = {(xi % yi, yi) for xi, yi in queries if yi <= sqrt(n)}
        
        for start_point, yi in pre_sum_array_keys: 
            _sum = nums[start_point]
            pre_sum_array[(start_point, yi)] = [0, _sum]
            for x in range(start_point + yi, n, yi):
                _sum += nums[x]
                pre_sum_array[(start_point, yi)].append(_sum)

        return [
            (
                big_y_pair_sums[(xi, yi)] 
                if yi > sqrt(n)
                else pre_sum_array[(xi % yi, yi)][-1] - pre_sum_array[(xi % yi, yi)][xi // yi]
            ) % mod
            for xi, yi in queries
        ]