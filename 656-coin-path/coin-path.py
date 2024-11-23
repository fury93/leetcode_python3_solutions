class Solution:
    def cheapestJump(self, A, B):
        if not A or A[0] == -1: return []
        dp = [[float('inf')] for _ in A]
        dp[0] = [A[0], 1]
        for j in range(1, len(A)):
            if A[j] == -1: continue
            dp[j] = min([dp[i][0] + A[j]] + dp[i][1:] + [j + 1] for i in range(max(0, j - B), j))
        return dp[-1][1:] if dp[-1][0] < float('inf') else []