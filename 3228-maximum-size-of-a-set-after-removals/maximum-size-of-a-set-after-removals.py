class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        set1, set2, maxLen = set(nums1), set(nums2), len(nums1) // 2
        uniqSet1 = set1 - set2
        uniqSet2 = set2 - set1
        intersectSet = set1 & set2
        uniqSet1Len = min(maxLen, len(uniqSet1))
        uniqSet2Len = min(maxLen, len(uniqSet2))
        return min(len(nums1), uniqSet1Len + uniqSet2Len + len(intersectSet) )
