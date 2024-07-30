class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleDigitsSum = doubleDigitsSum = 0
        for n in nums:
            if len(str(n)) == 1:
                singleDigitsSum += n
            else:
                doubleDigitsSum += n

        return singleDigitsSum != doubleDigitsSum