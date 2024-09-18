class Solution:
    # Kadane
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, max_so_far = 0, 0, float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            max_so_far = max(max_so_far, prefix, suffix)
        return max_so_far
    
    # Lee approach
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)