class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        Mod = 10**9+7
        dp = [0]*(maxLength+1)
        dp[0] = 1
        for i in range(1,maxLength+1):
            dp[i] = (dp[i-oneGroup]+dp[i-zeroGroup])%Mod

        return sum(dp[minLength:maxLength+1])%Mod

class Solution2:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        # MOD is the modulo constant for the result
        MOD = 10**9 + 7
        
        # Initializing a dynamic programming (dp) list to track the count of good binary strings 
        # of length i. Start with dp[0] = 1 since there's one way to create a binary string of length 0.
        dp = [0] * (maxLength + 1)
        dp[0] = 1

        # Iterate over possible string lengths from 1 to maxLength.
        for i in range(1, maxLength + 1):
            # If it's possible to append a group of ones of size oneGroup
            # to a previously shorter good string, then add that count to dp[i].
            if oneGroup <= i:
                dp[i] += dp[i - oneGroup]
            
            # Similarly, if it's possible to append a group of zeros of size zeroGroup
            # to a previously shorter good string, then add that count to dp[i].
            if zeroGroup <= i:
                dp[i] += dp[i - zeroGroup]

        # Return the sum of good binary strings of length between minLength and maxLength, inclusive.
        # Then, take the result modulo MOD to keep the number from getting too large.
        return sum(dp[minLength:maxLength+1]) % MOD