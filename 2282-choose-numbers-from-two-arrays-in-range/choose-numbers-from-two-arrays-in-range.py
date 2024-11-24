class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = int(1e9) + 7
        N = len(nums1)
        DP = defaultdict(int)
        ans = 0
        for i in range(N):
            n1 = nums1[i]
            n2 = nums2[i]
            DP2 = defaultdict(int)
            DP2[n1] += 1
            DP2[-n2] += 1
            
            for key, value in DP.copy().items():
                DP2[key + n1] = (DP2[key + n1] + value) % MOD
                DP2[key - n2] = (DP2[key - n2] + value) % MOD
            
            ans = (ans + DP2[0]) % MOD
            DP = DP2

        return ans