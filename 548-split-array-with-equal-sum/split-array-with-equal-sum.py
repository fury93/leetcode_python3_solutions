class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def split(A):
            total = sum(A)
            for i in range(1, len(A)): A[i] += A[i-1]
            return {A[i-1] for i in range(1, len(A)-1) if A[i-1] == total - A[i]}
            
        return len(nums) > 6 and any(split(nums[:j]) & split(nums[j+1:]) \
                             for j in range(3, len(nums)-3))
                             
class Solution2:
    def splitArray(self, A):
        P = [0]
        for x in A: P.append(P[-1] + x)
        
        N = len(A)
        Pinv = collections.defaultdict(list)
        for i, u in enumerate(P):
            Pinv[u].append(i)
            
        for j in range(1, N-1):
            for k in range(j+1, N-1):
                for i in Pinv[P[-1] - P[k+1]]:
                    if i >= j: break
                    if P[i] == P[j] - P[i+1] == P[k] - P[j+1]:
                        return True
        return False
        