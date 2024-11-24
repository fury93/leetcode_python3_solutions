class Solution:
    def numberOfWays(self, n: int, m: int, k: int, source: List[int], dest: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0]*4 for _ in range(k+1)]
        if source == dest:
            dp[0][0] = 1
        elif source[0] == dest[0]:
            dp[0][1] = 1
        elif source[1] == dest[1]:
            dp[0][2] = 1
        else:
            dp[0][3] = 1
        for i in range(1, k+1):
            dp[i][0] = (dp[i-1][1] + dp[i-1][2])%MOD
            dp[i][1] = (dp[i-1][0]*(m-1) + dp[i-1][1]*(m-2) + dp[i-1][3])%MOD
            dp[i][2] = (dp[i-1][0]*(n-1) + dp[i-1][2]*(n-2) + dp[i-1][3])%MOD
            dp[i][3] = (dp[i-1][1]*(n-1) + dp[i-1][2]*(m-1) + dp[i-1][3]*(m+n-4))%MOD
        return dp[k][0]

            