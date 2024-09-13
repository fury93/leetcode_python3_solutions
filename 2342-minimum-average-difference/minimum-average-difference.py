class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ln = len(nums)
        prefix = list(accumulate(nums))
        res = prefix[-1]//ln, ln - 1

        for i in range(ln-1):
            prefixAvg = prefix[i]//(i+1)
            suffixAvg = (prefix[-1] - prefix[i]) // (ln - i - 1)
            curRes = (abs(prefixAvg - suffixAvg), i)

            if curRes < res:
                res = curRes

        return res[1]

    def minimumAverageDifference2(self, nums: List[int]) -> int:
        sumEnd, sumFront, res, diff, n = 0, 0, 0, 1e9, len(nums)
        for num in nums:
            sumEnd += num

        for i in range(n):
            sumFront += nums[i]
            sumEnd -= nums[i]

            avg1 = sumEnd//(n-1-i) if i != n-1 else 0
            avg2 = sumFront//(i+1)

            if abs(avg1-avg2) < diff:
                diff = abs(avg1-avg2)
                res = i
        
        return res