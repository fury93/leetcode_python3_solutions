class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(x != y for x, y in zip(heights, sorted(heights)))

    def heightChecker2(self, heights: List[int]) -> int:
        map = collections.Counter(heights)
        res, j = 0, 0

        for i in range(len(heights)):
            while map[j] == 0:
                j +=1
            res += heights[i] != j
            map[j] -=1

        return res