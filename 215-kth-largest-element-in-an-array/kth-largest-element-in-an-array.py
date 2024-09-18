class Solution:
    # QuickSelect
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return nums[0]

        def findKthLargest(nums, k):
            pivot = random.choice(nums)
            left = [n for n in nums if n > pivot]
            mid = [n for n in nums if n == pivot]
            right = [n for n in nums if n < pivot]
            
            L, M = len(left), len(mid)
            
            if k <= L:
                return findKthLargest(left, k) # midIndex not included like most right element
            elif k > L + M:
                return findKthLargest(right, k - L - M)
            else:
                return mid[0]

        return findKthLargest(nums, k)
