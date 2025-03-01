# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution(object):
    def getIndex(self, reader):
        left = 0
        length = reader.length()
        while (length > 1):
            length //= 2
            cmp = reader.compareSub(left, left + length - 1, left + length,
                                              left + length + length - 1)
            if cmp == 0:
                return left + length + length
            if cmp < 0:
                left += length
        return left
        