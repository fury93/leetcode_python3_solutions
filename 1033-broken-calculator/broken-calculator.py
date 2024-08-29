class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # move from target to startValue, so use opposite operations / and +
        def calculate(x, y):
            if x == y: # no more operations needed
                return 0
            if y & 1: #it's the only one way to move to odd number from even
                return calculate(x, y+1) + 1
            if y > x:
                return calculate(x, y // 2) + 1
            else:
                return x - y

        return calculate(startValue, target)