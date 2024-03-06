class Solution:
    # BS solution
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        
        while low <= high:
            cur = (low + high) // 2
            count = sum(num <= cur for num in nums)
            
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
                
        return duplicate