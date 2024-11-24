class Solution:
    def divisibleTripletCount(self, A: List[int], d: int) -> int:
        ans = 0
        for i in range(len(A)):
            seen = Counter()
            for j in range(i+1, len(A)):
                ans += seen[-A[j]%d]
                seen[(A[i]+A[j])%d] += 1
        return ans