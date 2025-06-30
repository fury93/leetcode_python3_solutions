class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for key, val in cnt.items():
            res = max(res, val + cnt.get(key+1, -val))
        return res

    # todo not finished yet...lol
    def findLHS2(self, nums: List[int]) -> int:
        arr = sorted(nums)
        l, m, res = 0, 0, 0
        for r, val in enumerate(arr):
            if r > 0 and arr[r] != arr[r - 1]:
                m = r
            diff = abs(val - arr[l])
            if diff > 1:
                if l != m:
                    res = max(res, r - l + 1)
                l = r + 1

        return res