class Solution:
    def trap(self, h: List[int]) -> int:
        res, l, r = 0, 0, len(h) - 1
        lMax, rMax = 0, 0

        while l <= r:
            if h[l] < h[r]:
                lMax = max(lMax, h[l])
                res += lMax - h[l]
                l += 1
            else:
                rMax = max(rMax, h[r])
                res += rMax - h[r]
                r -= 1

        return res
