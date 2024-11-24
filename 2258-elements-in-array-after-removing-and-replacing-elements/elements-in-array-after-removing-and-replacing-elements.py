class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def answerQuery(query):
            time, idx = query
            time %= len(nums)*2
            if time <= len(nums):
                return nums[idx+time] if 0 <= idx+time < len(nums) else -1
            else:
                return nums[idx] if 0 <= idx < time-len(nums) else -1
        
        return [answerQuery(query) for query in queries]