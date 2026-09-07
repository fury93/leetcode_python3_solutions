class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
      
        # dp[i][j] represents the count of distinct subsequences ending with character 'a'+j
        # up to position i in the string
        dp = [[0] * 26 for _ in range(n + 1)]
      
        # Process each character in the string
        for i, char in enumerate(s, 1):
            # Convert character to index (0-25 for 'a'-'z')
            char_index = ord(char) - ord('a')
          
            # Update dp values for all 26 possible ending characters
            for j in range(26):
                if j == char_index:
                    # If current character matches, we can:
                    # 1. Append it to all previous subsequences (sum of dp[i-1])
                    # 2. Create a new single-character subsequence (+1)
                    dp[i][j] = (sum(dp[i - 1]) % MOD + 1) % MOD
                else:
                    # If character doesn't match, carry forward the previous count
                    dp[i][j] = dp[i - 1][j]
      
        # Return total count of distinct subsequences (sum of all ending possibilities)
        return sum(dp[-1]) % MOD
