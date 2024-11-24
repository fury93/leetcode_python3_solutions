# Definition of commonBits API.
# def commonBits(num: int) -> int:

class Solution:
    def findNumber(self):
        return reduce(lambda a, b: a | b,[1 << i  for i in range(30) if commonBits(1 << i) > commonBits(1 << i)])        