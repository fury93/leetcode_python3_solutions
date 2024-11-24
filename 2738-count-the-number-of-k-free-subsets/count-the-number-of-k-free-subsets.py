class Solution:
    def countTheNumOfKFreeSubsets(self, A: List[int], k: int) -> int:        
        dp = [1, 2] + [0] * 998
        for i in range(2, 1000):
            dp[i] = 1 + dp[i - 1] + dp[i - 2]

        A.sort()
        chains, cur_list = [], {}

        for a in A:
            if a - k in cur_list:
                cur_list[a - k].append(a)
                cur_list[a] = cur_list.pop(a - k)
            else:
                cur_list[a] = [a]
                chains.append(cur_list[a])

        res = [dp[len(chain) - 1] for chain in chains]

        return functools.reduce(lambda x,y: x * y, [a + 1 for a in res])