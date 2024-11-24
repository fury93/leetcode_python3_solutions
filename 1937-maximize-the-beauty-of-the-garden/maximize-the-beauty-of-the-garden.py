class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        positive_prefix_sum = [0]
        positions = {}
        maxsum = -inf

        for idx, flower in enumerate(flowers):
            positive_val = flower if flower >= 0 else 0
            negative_val = flower if flower < 0 else 0
            positive_prefix_sum += [positive_prefix_sum[-1] + positive_val]
            # in order to maximize the sum, we are only interested in
            # the first position of every element
            if not flower in positions:
                positions[flower] = idx
            else:
                # given that negative numbers are not part of the prefix sum,
                # we need to include them if they are the first / last items
                first_pos = positions[flower]
                newsum = 2 * negative_val + positive_prefix_sum[idx + 1] - positive_prefix_sum[first_pos]
        
                maxsum = max(maxsum, newsum)
        return maxsum