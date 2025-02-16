class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix, rightSm, leftSm = [], sum(nums), 0

        res = 0
        for i in range(len(nums)-1):
            leftSm += nums[i]
            rightSm -= nums[i]
            diff = abs(rightSm - leftSm)

            if diff & 1 == 0:
                res += 1
            
        return res


