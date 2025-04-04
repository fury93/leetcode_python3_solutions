class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        banned = banned + [n + 1]

        m = len(banned)
        start = 0 # set 0 as starting number, no impact on cum, but add an extra 1 into count
        cum = 0
        ans = -1 # remove 0 from count
        for i in range(m):
            end = banned[i] - 1
            if start <= end:
                cnt  = end - start + 1
                se = start + end
                tot = cnt  * se // 2
                if cum + tot <= maxSum:
                    ans += cnt 
                    cum += tot
                else:
                    # quadratic equation to solve, only one root > 0
                    # maxSum - cum = (end + start) * (end - start + 1) // 2
                    # end^2 + end + (start - start^2 - 2 * (maxSum - cum)) = 0
                    C = -start + start ** 2 + 2 * (maxSum - cum)
                    end = int((sqrt(4 * C + 1) - 1) / 2)
                    ans += end - start + 1
                    break
            start = banned[i] + 1

        return ans