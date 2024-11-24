class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)
        dp = [0] + [inf] * n
        for i in range(n):
            for w, c in zip(words, costs):
                if target[i:i+len(w)] == w:
                    dp[i+len(w)] = min(dp[i+len(w)], dp[i] + c)
        return dp[-1] if dp[-1] != inf else -1