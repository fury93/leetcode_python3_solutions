class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
        mod = 10 ** 9 + 7
        for i in range(k+1):
            dp[i][i] = 1
        for i in range(1, k+1):
            for j in range(i+1, n+1):
                dp[i][j] = (i * dp[i][j-1] + dp[i-1][j-1]) % mod
        return dp[k][n]